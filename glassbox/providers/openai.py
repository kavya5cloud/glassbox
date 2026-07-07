"""OpenAI client adapter for generating Glassbox traces."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from types import SimpleNamespace

from glassbox.tracing import EventBus, Trace
from glassbox.tracing.builder import TraceBuilder
from glassbox.tracing.bus import default_bus


class OpenAIInterceptor:
    """Wrap an OpenAI client instance and publish traces for responses.create calls."""

    def __init__(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def wrap(self, client: Any) -> Any:
        """Return a wrapped client instance."""
        return OpenAIInterceptor(client, event_bus=self._event_bus)


class OpenAIResponsesAdapter:
    """Adapter for the OpenAI responses API."""

    def __init__(self, client: Any, builder: TraceBuilder) -> None:
        self._client = client
        self._builder = builder

    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        trace = self._builder.build(
            provider="OpenAI",
            model=kwargs.get("model") or getattr(response, "model", "unknown"),
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def _extract_request_text(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def _extract_response_text(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def _extract_usage_value(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)
