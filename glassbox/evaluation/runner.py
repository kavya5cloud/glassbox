"""Evaluation orchestration.

Public API:
- EvaluationResult
- EvaluationRunner

Future extension points:
- parallel execution
- confidence calibration
- human review routing
"""

from __future__ import annotations

from dataclasses import dataclass

from glassbox.storage import Dataset

from .diff import Diff, diff_datasets
from .scorer import ConstantScorer, Score, Scorer


@dataclass(frozen=True, slots=True)
class EvaluationResult:
    """The output of a dataset comparison."""

    left_dataset_id: str
    right_dataset_id: str
    score: Score
    diff: Diff


class EvaluationRunner:
    """Coordinate scoring and diff generation."""

    def __init__(self, scorer: Scorer | None = None) -> None:
        self._scorer = scorer or ConstantScorer()

    @property
    def scorer(self) -> Scorer:
        """Return the active scorer."""

        return self._scorer

    def compare(self, left: Dataset, right: Dataset) -> EvaluationResult:
        """Compare two datasets and return a structured result."""

        score = self._scorer.score(left, right)
        return EvaluationResult(
            left_dataset_id=left.id,
            right_dataset_id=right.id,
            score=score,
            diff=diff_datasets(left, right),
        )
