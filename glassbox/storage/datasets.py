"""Dataset snapshots for evaluation and regression analysis.

Public API:
- Dataset
- DatasetStore
- MemoryDatasetStore

Future extension points:
- sampling metadata
- redaction provenance
- synthetic dataset promotion
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Protocol


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(frozen=True, slots=True)
class Dataset:
    """A versioned, immutable snapshot of sessions or observations."""

    id: str
    name: str
    session_ids: tuple[str, ...] = ()
    observation_ids: tuple[str, ...] = ()
    artifact_ids: tuple[str, ...] = ()
    created_at: datetime = field(default_factory=_utc_now)
    metadata: tuple[tuple[str, str], ...] = ()

    def __post_init__(self) -> None:
        if self.created_at.tzinfo is None or self.created_at.utcoffset() is None:
            raise ValueError("created_at must be timezone-aware")


class DatasetStore(Protocol):
    """Store datasets by identifier."""

    def put(self, dataset: Dataset) -> None:
        """Persist a dataset."""

    def get(self, dataset_id: str) -> Dataset | None:
        """Retrieve a dataset."""


class MemoryDatasetStore:
    """A simple in-memory dataset store."""

    def __init__(self) -> None:
        self._datasets: dict[str, Dataset] = {}

    def put(self, dataset: Dataset) -> None:
        self._datasets[dataset.id] = dataset

    def get(self, dataset_id: str) -> Dataset | None:
        return self._datasets.get(dataset_id)
