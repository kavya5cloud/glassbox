from __future__ import annotations

import json
import re
import subprocess
import threading
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def _run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=True)


def test_glassbox_help_lists_capture_command(tmp_path) -> None:
    result = _run(["glassbox", "--help"], cwd=tmp_path)

    assert "capture" in result.stdout
    assert "dataset" in result.stdout
    assert "eval" in result.stdout
    assert "diff" in result.stdout
    assert "watch" in result.stdout
    assert "demo" in result.stdout


def test_capture_help_is_available(tmp_path) -> None:
    result = _run(["glassbox", "capture", "--help"], cwd=tmp_path)

    assert "Usage: glassbox capture" in result.stdout
    assert "Command to execute under capture." in result.stdout


def test_dataset_help_is_available(tmp_path) -> None:
    result = _run(["glassbox", "dataset", "--help"], cwd=tmp_path)

    assert "Usage: glassbox dataset" in result.stdout
    assert "Create a dataset snapshot from an existing session." in result.stdout


def test_capture_runs_tiny_python_example_and_writes_session_files(tmp_path) -> None:
    examples_dir = tmp_path / "examples"
    examples_dir.mkdir()
    output_file = tmp_path / "example-ran.txt"
    script = examples_dir / "agent.py"
    script.write_text(
        "from pathlib import Path\n"
        f"Path({str(output_file)!r}).write_text('ran', encoding='utf-8')\n",
        encoding="utf-8",
    )

    result = _run(
        ["glassbox", "capture", sys.executable, "examples/agent.py"],
        cwd=tmp_path,
    )

    assert "Session created:" in result.stdout
    assert "Duration:" in result.stdout
    assert "Observations:" in result.stdout
    assert "Artifacts:" in result.stdout
    assert output_file.read_text(encoding="utf-8") == "ran"

    match = re.search(r"Session created:\n(?P<session_id>session-[^\n]+)", result.stdout)
    assert match is not None
    session_id = match.group("session_id")
    session_dir = tmp_path / ".glassbox" / "sessions" / session_id
    assert session_dir.exists()

    session_payload = json.loads((session_dir / "session.json").read_text(encoding="utf-8"))
    execution_payload = json.loads((session_dir / "execution.json").read_text(encoding="utf-8"))
    observations = [
        json.loads(line)
        for line in (session_dir / "observations.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    assert session_payload["id"] == session_id
    assert session_payload["state"] == "complete"
    assert session_payload["command"] == [sys.executable, "examples/agent.py"]
    assert session_payload["cwd"] == str(tmp_path)
    assert session_payload["duration_seconds"] >= 0
    assert session_payload["observation_ids"] == [event["id"] for event in observations]

    assert execution_payload["session_id"] == session_id
    assert execution_payload["state"] == "complete"
    assert execution_payload["exit_code"] == 0
    assert execution_payload["command"] == [sys.executable, "examples/agent.py"]
    assert execution_payload["cwd"] == str(tmp_path)
    assert execution_payload["duration_seconds"] >= 0

    assert [event["kind"] for event in observations] == ["process_started", "process_finished"]
    assert observations[0]["command"] == [sys.executable, "examples/agent.py"]
    assert observations[0]["cwd"] == str(tmp_path)
    assert observations[1]["exit_code"] == 0
    assert observations[1]["duration_seconds"] >= 0


def test_capture_records_http_requests_with_redacted_headers(tmp_path) -> None:
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self) -> None:  # noqa: N802
            body = b"hello from server"
            _ = self.rfile.read(int(self.headers.get("Content-Length", "0")))
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Set-Cookie", "session=secret")
            self.send_header("X-Auth-Token", "very-secret")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args) -> None:  # noqa: A003
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        port = server.server_address[1]
        examples_dir = tmp_path / "examples"
        examples_dir.mkdir()
        output_file = tmp_path / "http-example-ran.txt"
        script = examples_dir / "agent.py"
        script.write_text(
            "from pathlib import Path\n"
            "from urllib.request import Request, urlopen\n"
            f"url = 'http://127.0.0.1:{port}/capture'\n"
            "request = Request(\n"
            "    url,\n"
            "    data=b'payload',\n"
            "    headers={\n"
            "        'Authorization': 'secret-token',\n"
            "        'X-Api-Key': 'secret-key',\n"
            "    },\n"
            "    method='POST',\n"
            ")\n"
            "with urlopen(request, timeout=5) as response:\n"
            f"    Path({str(output_file)!r}).write_text(response.read().decode('utf-8'), encoding='utf-8')\n",
            encoding="utf-8",
        )

        result = _run(
            ["glassbox", "capture", sys.executable, "examples/agent.py"],
            cwd=tmp_path,
        )

        assert "Session created:" in result.stdout
        assert "Observations:" in result.stdout
        assert "Artifacts:" in result.stdout
        assert output_file.read_text(encoding="utf-8") == "hello from server"

        match = re.search(r"Session created:\n(?P<session_id>session-[^\n]+)", result.stdout)
        assert match is not None
        session_id = match.group("session_id")
        session_dir = tmp_path / ".glassbox" / "sessions" / session_id
        observations = [
            json.loads(line)
            for line in (session_dir / "observations.jsonl").read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        http_events = [event for event in observations if event["kind"] == "http_request"]

        assert len(observations) == 3
        assert len(http_events) == 1
        http_event = http_events[0]
        assert http_event["method"] == "POST"
        assert http_event["status_code"] == 200
        assert http_event["request_size"] == len(b"payload")
        assert http_event["response_size"] == len("hello from server".encode("utf-8"))
        assert http_event["request_headers"]["Authorization"] == "***redacted***"
        assert http_event["request_headers"]["X-Api-Key"] == "***redacted***"
        assert http_event["response_headers"]["Set-Cookie"] == "***redacted***"
        assert http_event["response_headers"]["X-Auth-Token"] == "***redacted***"
        assert http_event["response_headers"]["Content-Type"] == "text/plain"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)
