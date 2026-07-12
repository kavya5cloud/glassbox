from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID

from glassbox.tracing.trace import Trace


def test_trace_defaults_are_stable_and_serializable() -> None:
    trace = Trace()

    assert trace.provider == "unknown"
    assert trace.model == "unknown"
    assert trace.status == "running"
    assert isinstance(trace.id, UUID)
    assert trace.started_at.tzinfo is not None

    payload = trace.to_dict()
    assert payload["id"] == str(trace.id)
    assert payload["started_at"].endswith("Z")
    assert datetime.fromisoformat(payload["started_at"].replace("Z", "+00:00")) == trace.started_at
    assert payload["ended_at"] is None


def test_trace_preserves_unicode_and_emojis_through_serialization() -> None:
    trace = Trace(
        provider="OpenAI",
        model="gpt-4.1",
        prompt="Olá 👋",
        response="结果是正确的 ✅",
        started_at=datetime(2026, 7, 11, 4, 0, tzinfo=timezone.utc),
        ended_at=datetime(2026, 7, 11, 4, 0, 1, tzinfo=timezone.utc),
    )

    payload = trace.to_dict()

    assert payload["prompt"] == "Olá 👋"
    assert payload["response"] == "结果是正确的 ✅"
