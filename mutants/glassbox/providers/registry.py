"""Backward-compatible import shim for the provider manager."""

from __future__ import annotations

from .manager import available_adapters, get_adapter_for_client, register_adapter

__all__ = ["available_adapters", "get_adapter_for_client", "register_adapter"]
