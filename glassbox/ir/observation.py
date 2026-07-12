"""Immutable observations for the IR profile boundary."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _stringify(value: Any) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, (list, tuple, dict)):
        return json.dumps(value, sort_keys=True, default=str)
    return str(value)


@dataclass(frozen=True, slots=True)
class Observation:
    """A normalized, immutable observation."""

    id: str
    kind: str
    occurred_at: datetime = field(default_factory=_utc_now)
    fields: tuple[tuple[str, str], ...] = ()
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.occurred_at.tzinfo is None or self.occurred_at.utcoffset() is None:
            raise ValueError("occurred_at must be timezone-aware")

    @classmethod
    def from_mapping(
        cls,
        payload: Mapping[str, Any],
        *,
        fields: tuple[str, ...] | None = None,
    ) -> "Observation":
        """Create an immutable observation from a mapping."""

        selected = fields or tuple(key for key in payload.keys() if key not in {"id", "kind", "occurred_at"})
        normalized = tuple((key, _stringify(payload[key])) for key in selected if key in payload)
        occurred_at = payload["occurred_at"]
        if isinstance(occurred_at, str):
            occurred_at = datetime.fromisoformat(occurred_at)
        return cls(
            id=str(payload["id"]),
            kind=str(payload["kind"]),
            occurred_at=occurred_at,
            fields=normalized,
        )

    def get(self, key: str, default: str = "") -> str:
        """Return a field value or a default."""

        for field_name, value in self.fields:
            if field_name == key:
                return value
        return default
