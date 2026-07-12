"""Identity records in the Glassbox IR."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True, slots=True)
class Identity:
    """A stable IR identity."""

    id: str
    kind: str = "session"
    metadata: tuple[tuple[str, str], ...] = ()

    @property
    def digest(self) -> str:
        """Return a deterministic identity digest."""

        payload = "|".join([self.id, self.kind, ",".join(f"{k}={v}" for k, v in self.metadata)])
        return sha256(payload.encode("utf-8")).hexdigest()
