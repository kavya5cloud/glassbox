"""Relations between immutable core objects.

Public API:
- RelationKind
- Relation

Future extension points:
- causal edge annotations
- confidence scores
- graph materialization
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

RelationKind: TypeAlias = Literal["causal", "derived_from", "belongs_to", "parent_of", "related_to"]


@dataclass(frozen=True, slots=True)
class Relation:
    """A directed edge between two core identifiers."""

    source_id: str
    target_id: str
    kind: RelationKind
    metadata: tuple[tuple[str, str], ...] = ()
