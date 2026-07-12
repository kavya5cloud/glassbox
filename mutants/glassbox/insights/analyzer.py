"""Insight analyzer for traces."""

from __future__ import annotations

from collections.abc import Sequence

from glassbox.tracing import Trace

from .models import Insight, SessionStatistics
from .rules import DEFAULT_RULES, InsightRule


class InsightAnalyzer:
    """Run a deterministic set of insight rules over a trace."""

    def __init__(self, rules: Sequence[InsightRule] = DEFAULT_RULES) -> None:
        self._rules = tuple(rules)

    def analyze(
        self,
        trace: Trace,
        session_stats: SessionStatistics | None = None,
    ) -> list[Insight]:
        """Return the ordered list of insights produced for a trace."""
        insights: list[Insight] = []
        for rule in self._rules:
            insight = rule(trace, session_stats)
            if insight is not None:
                insights.append(insight)
        return insights
