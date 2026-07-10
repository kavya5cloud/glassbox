"""Azure OpenAI provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


class AzureOpenAIAdapter(PassThroughProviderAdapter):
    """Adapter stub for Azure OpenAI clients."""

    provider_name = "Azure OpenAI"

    @classmethod
    def supports(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or "").lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")


register_adapter(AzureOpenAIAdapter)
