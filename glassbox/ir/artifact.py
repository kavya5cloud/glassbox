"""Artifacts in the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TypeAlias

ArtifactKind: TypeAlias = str


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Artifact:
    """A durable IR artifact."""

    id: str
    kind: ArtifactKind
    content_ref: str
    created_at: datetime = field(default_factory=_utc_now)
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None or self.created_at.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")
