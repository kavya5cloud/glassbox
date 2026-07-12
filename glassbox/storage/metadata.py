"""Metadata storage for derived artifacts and catalogs.

Public API:
- MetadataEntry
- MetadataStore
- MemoryMetadataStore

Future extension points:
- indexed lookups
- retention filtering
- policy enforcement
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class MetadataEntry:
    """A stable set of metadata associated with a domain identifier."""

    entity_id: str
    fields: tuple[tuple[str, str], ...] = ()


class MetadataStore(Protocol):
    """Store metadata entries for later lookup."""

    def put(self, entry: MetadataEntry) -> None:
        """Persist an entry."""

    def get(self, entity_id: str) -> MetadataEntry | None:
        """Retrieve an entry."""


class MemoryMetadataStore:
    """A simple in-memory metadata store."""

    def __init__(self) -> None:
        self._entries: dict[str, MetadataEntry] = {}

    def put(self, entry: MetadataEntry) -> None:
        self._entries[entry.entity_id] = entry

    def get(self, entity_id: str) -> MetadataEntry | None:
        return self._entries.get(entity_id)
