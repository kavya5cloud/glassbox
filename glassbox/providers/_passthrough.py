"""Shared helpers for provider adapters that currently pass clients through."""

from __future__ import annotations

from typing import Any

from glassbox.tracing.bus import EventBus


class PassThroughProviderAdapter:
    """Base class for provider stubs that do not yet intercept traffic."""

    provider_name = "unknown"

    @classmethod
    def supports(cls, client: Any) -> bool:
        """Return whether this adapter can wrap the client."""
        return False

    @classmethod
    def wrap(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return the original client unchanged."""
        return client
