"""Evaluation engine primitives.

Public API:
- Score
- Scorer
- ConstantScorer
- Diff
- EvaluationResult
- EvaluationRunner

Future extension points:
- human review scoring
- risk calibration
- deployment recommendations
"""

from .diff import Diff
from .runner import EvaluationResult, EvaluationRunner
from .scorer import ConstantScorer, Score, Scorer

__all__ = [
    "ConstantScorer",
    "Diff",
    "EvaluationResult",
    "EvaluationRunner",
    "Score",
    "Scorer",
]
