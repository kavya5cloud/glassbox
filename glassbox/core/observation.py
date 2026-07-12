"""Immutable observation records.

Public API:
- ObservationKind
- Observation

Future extension points:
- payload codecs
- schema evolution
- observation segmentation for streaming
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import TypeAlias

ObservationKind: TypeAlias = str


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Observation:
    """A single immutable fact captured from runtime execution."""

    id: str
    session_id: str
    run_id: str
    kind: ObservationKind
    payload_ref: str
    identity_ref: str
    occurred_at: datetime = field(default_factory=_utc_now)
    parent_id: str | None = None
    relation_ids: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")

    def to_dict(self) -> dict[str, object]:
        """Return a JSON-friendly representation of the observation."""

        return {
            "id": self.id,
            "session_id": self.session_id,
            "run_id": self.run_id,
            "kind": self.kind,
            "payload_ref": self.payload_ref,
            "identity_ref": self.identity_ref,
            "occurred_at": self.occurred_at.isoformat(),
            "parent_id": self.parent_id,
            "relation_ids": self.relation_ids,
            "metadata": self.metadata,
        }
