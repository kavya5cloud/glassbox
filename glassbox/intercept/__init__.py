"""Interceptor helpers for wrapping provider clients."""

from __future__ import annotations

from typing import Any

from glassbox.providers.openai import OpenAIInterceptor
from glassbox.tracing.bus import EventBus


def intercept(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    if hasattr(client, "responses"):
        return OpenAIInterceptor(client, event_bus=event_bus)

    return client
