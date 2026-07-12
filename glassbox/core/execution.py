"""Execution records for runs and re-executions.

Public API:
- ExecutionState
- Execution

Future extension points:
- divergence markers
- simulation metadata
- side-effect classification
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone
from typing import Literal, TypeAlias

ExecutionState: TypeAlias = Literal[
    "planned",
    "running",
    "complete",
    "diverged",
    "failed",
]


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Execution:
    """A single execution attempt for a session or experiment."""

    id: str
    session_id: str
    identity_ref: str
    state: ExecutionState = "planned"
    started_at: datetime = field(default_factory=_utc_now)
    ended_at: datetime | None = None
    observation_ids: tuple[str, ...] = ()
    artifact_ids: tuple[str, ...] = ()
    parent_execution_id: str | None = None
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.started_at.tzinfo is None or self.started_at.utcoffset() is None:
            raise ValueError("started_at must be timezone-aware")
        if self.ended_at is not None and (
            self.ended_at.tzinfo is None or self.ended_at.utcoffset() is None
        ):
            raise ValueError("ended_at must be timezone-aware when provided")

    @classmethod
    def running(cls, id: str, session_id: str, identity_ref: str) -> "Execution":
        """Create an execution that has started but not yet ended."""

        return cls(id=id, session_id=session_id, identity_ref=identity_ref, state="running")

    def complete(self, *, ended_at: datetime | None = None) -> "Execution":
        """Return a completed copy of the execution."""

        return replace(self, state="complete", ended_at=ended_at or _utc_now())
