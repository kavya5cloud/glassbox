"""Executions in the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import datetime, timezone


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Execution:
    """A single IR execution."""

    id: str
    identity_id: str
    started_at: datetime = field(default_factory=_utc_now)
    ended_at: datetime | None = None
    command: tuple[str, ...] = ()
    cwd: str = ""
    exit_code: int | None = None
    node_ids: tuple[str, ...] = ()
    artifact_ids: tuple[str, ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.started_at.tzinfo is None or self.started_at.utcoffset() is None:
            raise ValueError("started_at must be timezone-aware")
        if self.ended_at is not None and (
            self.ended_at.tzinfo is None or self.ended_at.utcoffset() is None
        ):
            raise ValueError("ended_at must be timezone-aware when provided")

    def close(self, *, ended_at: datetime | None = None, exit_code: int | None = None) -> "Execution":
        """Return a completed copy."""

        return replace(self, ended_at=ended_at or _utc_now(), exit_code=exit_code)
