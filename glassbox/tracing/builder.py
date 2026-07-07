"""Builds Trace objects from provider-specific response data."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from glassbox.tracing import Trace
from glassbox.tracing.bus import EventBus, default_bus


class TraceBuilder:
    """Convert provider-specific data into a Trace and publish it."""

    def __init__(self, event_bus: EventBus | None = None) -> None:
        self._event_bus = event_bus or default_bus

    def build(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def publish(self, trace: Trace) -> None:
        """Publish a built trace through the configured event bus."""
        self._event_bus.publish(trace)
