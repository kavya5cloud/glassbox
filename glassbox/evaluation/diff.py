"""Structured diffs for dataset comparisons.

Public API:
- Diff
- diff_datasets

Future extension points:
- semantic change classification
- token/cost deltas
- confidence scoring
"""

from __future__ import annotations

from dataclasses import dataclass

from glassbox.storage import Dataset


@dataclass(frozen=True, slots=True)
class Diff:
    """A human- and machine-readable comparison summary."""

    left_id: str
    right_id: str
    added_session_ids: tuple[str, ...] = ()
    removed_session_ids: tuple[str, ...] = ()
    added_observation_ids: tuple[str, ...] = ()
    removed_observation_ids: tuple[str, ...] = ()
    confidence: float = 1.0
    summary: str = ""


def diff_datasets(left: Dataset, right: Dataset) -> Diff:
    """Compute a simple deterministic dataset diff."""

    left_sessions = set(left.session_ids)
    right_sessions = set(right.session_ids)
    left_observations = set(left.observation_ids)
    right_observations = set(right.observation_ids)

    return Diff(
        left_id=left.id,
        right_id=right.id,
        added_session_ids=tuple(sorted(right_sessions - left_sessions)),
        removed_session_ids=tuple(sorted(left_sessions - right_sessions)),
        added_observation_ids=tuple(sorted(right_observations - left_observations)),
        removed_observation_ids=tuple(sorted(left_observations - right_observations)),
        summary=f"Compared datasets {left.name} and {right.name}",
    )
