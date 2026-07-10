"""Provider adapters for intercepting LLM client calls."""

from .base import ProviderAdapter
from .manager import available_adapters, get_adapter_for_client, register_adapter

__all__ = [
    "ProviderAdapter",
    "available_adapters",
    "get_adapter_for_client",
    "register_adapter",
]
