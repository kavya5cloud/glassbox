"""Anthropic provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


class AnthropicAdapter(PassThroughProviderAdapter):
    """Adapter stub for Anthropic clients."""

    provider_name = "Anthropic"

    @classmethod
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "messages")


register_adapter(AnthropicAdapter)
