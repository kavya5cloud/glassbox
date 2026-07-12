"""Immutable artifacts derived from sessions and observations.

Public API:
- ArtifactKind
- Artifact

Future extension points:
- artifact signing
- artifact provenance
- artifact compression hints
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal, TypeAlias

ArtifactKind: TypeAlias = Literal["blob", "dataset", "diff", "evaluation", "semantic_view", "report"]


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Artifact:
    """A durable derived object that can be recomputed from raw observations."""

    id: str
    kind: ArtifactKind
    content_ref: str
    created_at: datetime = field(default_factory=_utc_now)
    session_id: str | None = None
    run_id: str | None = None
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None or self.created_at.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")
