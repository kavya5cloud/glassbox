"""Public SDK entry points.

Public API:
- Glassbox

Future extension points:
- transport attachment
- session factories
- experiment builders
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from datetime import datetime, timezone

from glassbox.core import IdentityFingerprint, Session


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Glassbox:
    """Immutable SDK context that carries identity and optional session state."""

    identity: IdentityFingerprint
    session: Session | None = None

    @classmethod
    def blank(cls) -> "Glassbox":
        """Return a bootstrap context with an empty identity."""

        return cls(identity=IdentityFingerprint.blank())

    def open_session(
        self,
        session_id: str,
        *,
        started_at: datetime | None = None,
        metadata: tuple[tuple[str, str], ...] = (),
    ) -> "Glassbox":
        """Return a new SDK context with an active session."""

        session = Session(
            id=session_id,
            identity_ref=self.identity.digest,
            started_at=started_at or _utc_now(),
            state="running",
            metadata=metadata,
        )
        return replace(self, session=session)

    def close_session(self, *, ended_at: datetime | None = None) -> "Glassbox":
        """Return a new SDK context with a completed session when one exists."""

        if self.session is None:
            return self
        return replace(self, session=self.session.close(ended_at=ended_at))
