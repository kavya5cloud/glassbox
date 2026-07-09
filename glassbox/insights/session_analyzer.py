"""Session-level analyzer for generating reusable summary insights."""

from __future__ import annotations

from collections.abc import Sequence

from glassbox.tracing import Trace

from .models import Insight, SessionStatistics
from .session_rules import DEFAULT_SESSION_RULES, SessionInsightRule


class SessionAnalyzer:
    """Run a deterministic set of session-level insight rules."""

    def __init__(self, rules: Sequence[SessionInsightRule] = DEFAULT_SESSION_RULES) -> None:
        self._rules = tuple(rules)

    def analyze(
        self,
        traces: Sequence[Trace],
        session_stats: SessionStatistics | None = None,
    ) -> list[Insight]:
        insights: list[Insight] = []
        for rule in self._rules:
            insight = rule(traces, session_stats)
            if insight is not None:
                insights.append(insight)
        return insights
