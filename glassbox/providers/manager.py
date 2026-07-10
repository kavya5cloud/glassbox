"""Registry and discovery helpers for provider adapters."""

from __future__ import annotations

from importlib import import_module
from pkgutil import iter_modules
from typing import Any

from .base import ProviderAdapter

_registered_adapters: list[type[ProviderAdapter]] = []
_discovered = False


def register_adapter(adapter: type[ProviderAdapter]) -> type[ProviderAdapter]:
    """Register a provider adapter class for later discovery."""
    if adapter not in _registered_adapters:
        _registered_adapters.append(adapter)
    return adapter


def _discover_builtin_adapters() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def available_adapters() -> tuple[type[ProviderAdapter], ...]:
    """Return all registered adapters, importing built-ins on first use."""
    _discover_builtin_adapters()
    return tuple(_registered_adapters)


def get_adapter_for_client(client: Any) -> type[ProviderAdapter] | None:
    """Return the first registered adapter that supports the given client."""
    for adapter in available_adapters():
        if adapter.supports(client):
            return adapter
    return None
