"""Edges in the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TypeAlias

EdgeKind: TypeAlias = str


@dataclass(frozen=True, slots=True)
class Edge:
    """A directed IR edge."""

    source_id: str
    target_id: str
    kind: EdgeKind
    metadata: tuple[tuple[str, str], ...] = ()
