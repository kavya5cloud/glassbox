"""Reusable insight engine for turning traces into developer-facing signals."""

from .analyzer import InsightAnalyzer
from .models import Insight, InsightSeverity, SessionStatistics
from .session_analyzer import SessionAnalyzer
from .rules import DEFAULT_RULES
from .session_rules import DEFAULT_SESSION_RULES

__all__ = [
    "DEFAULT_RULES",
    "DEFAULT_SESSION_RULES",
    "Insight",
    "InsightAnalyzer",
    "InsightSeverity",
    "SessionAnalyzer",
    "SessionStatistics",
]
