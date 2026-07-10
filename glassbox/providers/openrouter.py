"""OpenRouter provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


class OpenRouterAdapter(PassThroughProviderAdapter):
    """Adapter stub for OpenRouter clients."""

    provider_name = "OpenRouter"

    @classmethod
    def supports(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()


register_adapter(OpenRouterAdapter)
