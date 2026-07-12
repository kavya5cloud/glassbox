from __future__ import annotations

from datetime import datetime, timezone

from glassbox.tracing.builder import TraceBuilder
from glassbox.tracing.bus import EventBus


def test_trace_builder_computes_latency_and_publishes_trace() -> None:
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)
    builder = TraceBuilder(event_bus=bus)
    started_at = datetime(2026, 7, 11, 4, 0, 0, tzinfo=timezone.utc)
    ended_at = datetime(2026, 7, 11, 4, 0, 1, 250_000, tzinfo=timezone.utc)

    trace = builder.build(
        provider="OpenAI",
        model="gpt-4.1",
        prompt="Hello",
        response_text="World",
        input_tokens=12,
        output_tokens=7,
        started_at=started_at,
        ended_at=ended_at,
    )
    builder.publish(trace)

    assert trace.latency_ms == 1250
    assert trace.cost == 0.0
    assert trace.started_at == started_at
    assert trace.ended_at == ended_at
    assert received == [trace]


def test_trace_builder_respects_explicit_latency_and_cost() -> None:
    builder = TraceBuilder()

    trace = builder.build(
        provider="Anthropic",
        model="claude",
        prompt="Prompt",
        response_text="Response",
        input_tokens=1,
        output_tokens=2,
        latency_ms=42,
        cost=0.1234,
    )

    assert trace.latency_ms == 42
    assert trace.cost == 0.1234
