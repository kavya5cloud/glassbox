"""HTTP capture bootstrap for Glassbox subprocesses."""

from __future__ import annotations

import json
import os
import threading
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Iterator, Mapping
from uuid import uuid4

import http.client

_SENSITIVE_HEADERS = {
    "authorization",
    "proxy-authorization",
    "cookie",
    "set-cookie",
    "x-api-key",
    "x-auth-token",
    "x-authorization",
}

_CAPTURE_LOCK = threading.Lock()
_INSTALLED = False
_OBSERVATIONS_PATH: Path | None = None
_SESSION_ID: str | None = None
_EXECUTION_ID: str | None = None
_ORIGINAL_HTTP_REQUEST = http.client.HTTPConnection.request
_ORIGINAL_HTTPS_REQUEST = http.client.HTTPSConnection.request
_ORIGINAL_HTTP_GETRESPONSE = http.client.HTTPConnection.getresponse
_ORIGINAL_HTTPS_GETRESPONSE = http.client.HTTPSConnection.getresponse


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _redact(value: str) -> str:
    return "***redacted***" if value else value


def _redact_headers(headers: Mapping[str, Any] | None) -> dict[str, str]:
    redacted: dict[str, str] = {}
    if headers is None:
        return redacted
    for key, value in headers.items():
        header_name = str(key)
        header_value = str(value)
        if header_name.lower() in _SENSITIVE_HEADERS:
            redacted[header_name] = _redact(header_value)
        else:
            redacted[header_name] = header_value
    return redacted


def _body_size(body: Any) -> int:
    if body is None:
        return 0
    if isinstance(body, str):
        return len(body.encode("utf-8"))
    if isinstance(body, (bytes, bytearray, memoryview)):
        return len(body)
    return 0


def _append_observation(payload: dict[str, Any]) -> None:
    if _OBSERVATIONS_PATH is None:
        return
    with _CAPTURE_LOCK:
        _OBSERVATIONS_PATH.parent.mkdir(parents=True, exist_ok=True)
        with _OBSERVATIONS_PATH.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, sort_keys=True) + "\n")


def _observation_payload(
    *,
    kind: str,
    method: str,
    url: str,
    status_code: int | None,
    request_headers: dict[str, str],
    response_headers: dict[str, str],
    request_size: int,
    response_size: int,
    duration_seconds: float,
) -> dict[str, Any]:
    return {
        "id": f"observation-{uuid4().hex[:12]}",
        "session_id": _SESSION_ID,
        "execution_id": _EXECUTION_ID,
        "kind": kind,
        "occurred_at": _utc_now().isoformat(),
        "method": method,
        "url": url,
        "status_code": status_code,
        "duration_seconds": duration_seconds,
        "request_headers": request_headers,
        "response_headers": response_headers,
        "request_size": request_size,
        "response_size": response_size,
    }


@dataclass
class _CapturedResponse:
    response: http.client.HTTPResponse
    state: dict[str, Any]
    _response_size: int = 0
    _finalized: bool = False

    def _finalize(self) -> None:
        if self._finalized:
            return
        self._finalized = True
        ended_at = time.perf_counter()
        response_headers = _redact_headers({key: value for key, value in self.response.getheaders()})
        payload = _observation_payload(
            kind="http_request",
            method=self.state["method"],
            url=self.state["url"],
            status_code=getattr(self.response, "status", None),
            request_headers=self.state["request_headers"],
            response_headers=response_headers,
            request_size=self.state["request_size"],
            response_size=self._response_size
            or int(response_headers.get("Content-Length", "0") or 0),
            duration_seconds=ended_at - self.state["started_at"],
        )
        _append_observation(payload)

    def read(self, amt: int | None = None) -> bytes:
        data = self.response.read(amt)
        self._response_size += len(data)
        if amt is None or not data:
            self._finalize()
        return data

    def readinto(self, b: bytearray | memoryview) -> int:
        read = self.response.readinto(b)
        if read is None:
            read = 0
        self._response_size += read
        if read == 0:
            self._finalize()
        return read

    def close(self) -> None:
        try:
            self._finalize()
        finally:
            self.response.close()

    def __iter__(self) -> Iterator[bytes]:
        try:
            for chunk in self.response:
                self._response_size += len(chunk)
                yield chunk
        finally:
            self._finalize()

    def __getattr__(self, name: str) -> Any:
        return getattr(self.response, name)

    def __enter__(self) -> "_CapturedResponse":
        self.response.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self._finalize()
        self.response.__exit__(exc_type, exc, tb)


def _capture_request(
    connection: http.client.HTTPConnection,
    original_request: Callable[..., Any],
    method: str,
    url: str,
    body: Any = None,
    headers: Mapping[str, Any] | None = None,
    *,
    encode_chunked: bool = False,
) -> Any:
    state = {
        "started_at": time.perf_counter(),
        "method": method,
        "url": url,
        "request_headers": _redact_headers(headers),
        "request_size": _body_size(body),
    }
    setattr(connection, "_glassbox_http_state", state)
    return original_request(method, url, body=body, headers=headers, encode_chunked=encode_chunked)


def _capture_getresponse(
    connection: http.client.HTTPConnection,
    original_getresponse: Callable[..., http.client.HTTPResponse],
    *args: Any,
    **kwargs: Any,
) -> http.client.HTTPResponse | _CapturedResponse:
    response = original_getresponse(*args, **kwargs)
    state = getattr(connection, "_glassbox_http_state", None)
    if state is None:
        return response
    return _CapturedResponse(response=response, state=state)


def install_http_capture() -> None:
    """Install HTTP capture hooks for the current Python process."""

    global _INSTALLED, _OBSERVATIONS_PATH, _SESSION_ID, _EXECUTION_ID
    if _INSTALLED:
        return
    observations_path = os.environ.get("GLASSBOX_OBSERVATIONS_PATH")
    session_id = os.environ.get("GLASSBOX_SESSION_ID")
    execution_id = os.environ.get("GLASSBOX_EXECUTION_ID")
    if not observations_path or not session_id or not execution_id:
        return

    _OBSERVATIONS_PATH = Path(observations_path)
    _SESSION_ID = session_id
    _EXECUTION_ID = execution_id

    def http_request(
        self: http.client.HTTPConnection,
        method: str,
        url: str,
        body: Any = None,
        headers: Mapping[str, Any] | None = None,
        *,
        encode_chunked: bool = False,
    ) -> Any:
        return _capture_request(
            self,
            _ORIGINAL_HTTP_REQUEST.__get__(self, type(self)),
            method,
            url,
            body,
            headers,
            encode_chunked=encode_chunked,
        )

    def https_request(
        self: http.client.HTTPSConnection,
        method: str,
        url: str,
        body: Any = None,
        headers: Mapping[str, Any] | None = None,
        *,
        encode_chunked: bool = False,
    ) -> Any:
        return _capture_request(
            self,
            _ORIGINAL_HTTPS_REQUEST.__get__(self, type(self)),
            method,
            url,
            body,
            headers,
            encode_chunked=encode_chunked,
        )

    def http_getresponse(self: http.client.HTTPConnection, *args: Any, **kwargs: Any) -> Any:
        return _capture_getresponse(
            self,
            _ORIGINAL_HTTP_GETRESPONSE.__get__(self, type(self)),
            *args,
            **kwargs,
        )

    def https_getresponse(self: http.client.HTTPSConnection, *args: Any, **kwargs: Any) -> Any:
        return _capture_getresponse(
            self,
            _ORIGINAL_HTTPS_GETRESPONSE.__get__(self, type(self)),
            *args,
            **kwargs,
        )

    http.client.HTTPConnection.request = http_request  # type: ignore[assignment]
    http.client.HTTPSConnection.request = https_request  # type: ignore[assignment]
    http.client.HTTPConnection.getresponse = http_getresponse  # type: ignore[assignment]
    http.client.HTTPSConnection.getresponse = https_getresponse  # type: ignore[assignment]
    _INSTALLED = True
