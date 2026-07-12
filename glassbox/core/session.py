"""Session records.

Public API:
- SessionState
- Session

Future extension points:
- session lifecycle policies
- parent/child session trees
- resumable sessions
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Literal, TypeAlias

SessionState: TypeAlias = Literal[
    "planned",
    "running",
    "complete",
    "failed",
]


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Session:
    """A stateful AI task that may span many observations and runs."""

    id: str
    identity_ref: str
    started_at: datetime = field(default_factory=_utc_now)
    state: SessionState = "planned"
    run_ids: tuple[str, ...] = ()
    observation_ids: tuple[str, ...] = ()
    artifact_ids: tuple[str, ...] = ()
    parent_session_id: str | None = None
    metadata: tuple[tuple[str, str], ...] = ()
    ended_at: datetime | None = None

    def __post_init__(self) -> None:
        if self.started_at.tzinfo is None or self.started_at.utcoffset() is None:
            raise ValueError("started_at must be timezone-aware")
        if self.ended_at is not None and (
            self.ended_at.tzinfo is None or self.ended_at.utcoffset() is None
        ):
            raise ValueError("ended_at must be timezone-aware when provided")

    @classmethod
    def open(
        cls,
        id: str,
        identity_ref: str,
        *,
        metadata: tuple[tuple[str, str], ...] = (),
    ) -> "Session":
        """Create a running session with no observations yet."""

        return cls(id=id, identity_ref=identity_ref, state="running", metadata=metadata)

    def close(self, *, ended_at: datetime | None = None) -> "Session":
        """Return a completed copy of the session."""

        return replace(self, state="complete", ended_at=ended_at or _utc_now())
