"""Nodes in the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import TypeAlias

NodeKind: TypeAlias = str


@dataclass(frozen=True, slots=True)
class Node:
    """A typed IR node produced by a profile."""

    id: str
    kind: NodeKind
    occurred_at: datetime
    execution_id: str | None = None
    identity_id: str | None = None
    attributes: tuple[tuple[str, str], ...] = ()
    artifact_ids: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")
