"""Interceptor helpers for wrapping provider clients."""

from __future__ import annotations

from typing import Any

from glassbox.providers.manager import get_adapter_for_client
from glassbox.tracing.bus import EventBus


def intercept(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client
