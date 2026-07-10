"""Base interfaces for provider adapters."""

from __future__ import annotations

from typing import Any, Protocol

from glassbox.tracing.bus import EventBus


class ProviderAdapter(Protocol):
    """Protocol for provider adapters that wrap client instances."""

    provider_name: str

    @classmethod
    def supports(cls, client: Any) -> bool:
        """Return ``True`` when this adapter can wrap the given client."""
        ...

    @classmethod
    def wrap(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        ...
