"""Base interfaces for provider adapters."""

from __future__ import annotations

from typing import Any, Protocol


class ProviderAdapter(Protocol):
    """Protocol for provider adapters that wrap client instances."""

    def wrap(self, client: Any) -> Any:
        """Return a wrapped client instance."""
        ...
