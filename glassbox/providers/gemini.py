"""Gemini provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


class GeminiAdapter(PassThroughProviderAdapter):
    """Adapter stub for Gemini clients."""

    provider_name = "Gemini"

    @classmethod
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, "models")


register_adapter(GeminiAdapter)
