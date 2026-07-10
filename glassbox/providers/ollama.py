"""Ollama provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


class OllamaAdapter(PassThroughProviderAdapter):
    """Adapter stub for Ollama clients."""

    provider_name = "Ollama"

    @classmethod
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, "generate")


register_adapter(OllamaAdapter)
