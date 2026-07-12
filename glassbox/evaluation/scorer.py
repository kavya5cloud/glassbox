"""Scoring primitives for evaluations.

Public API:
- Score
- Scorer
- ConstantScorer

Future extension points:
- rubric scoring
- model-as-judge
- human review aggregation
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from glassbox.storage import Dataset


@dataclass(frozen=True, slots=True)
class Score:
    """A numeric score and explanation."""

    name: str
    value: float
    rationale: str = ""


class Scorer(Protocol):
    """Compute a score for a dataset comparison."""

    def score(self, left: Dataset, right: Dataset) -> Score:
        """Score a left/right comparison."""


@dataclass(frozen=True, slots=True)
class ConstantScorer:
    """A deterministic baseline scorer for bootstrapping."""

    name: str = "baseline"
    value: float = 1.0

    def score(self, left: Dataset, right: Dataset) -> Score:
        return Score(
            name=self.name,
            value=self.value,
            rationale=f"baseline comparison for {left.id} vs {right.id}",
        )
