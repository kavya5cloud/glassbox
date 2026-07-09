"""Pure, deterministic rules that convert traces into insights."""

from __future__ import annotations

from collections.abc import Callable

from glassbox.tracing import Trace

from .models import Insight, InsightSeverity, SessionStatistics

InsightRule = Callable[[Trace, SessionStatistics | None], Insight | None]

SLOW_REQUEST_THRESHOLD_MS = 5_000
LARGE_PROMPT_THRESHOLD_TOKENS = 10_000


def slow_request_rule(trace: Trace, _: SessionStatistics | None = None) -> Insight | None:
    """Flag requests that take longer than the slow-request threshold."""
    if trace.latency_ms <= SLOW_REQUEST_THRESHOLD_MS:
        return None

    return Insight(
        title="Slow Request",
        description=f"Latency reached {trace.latency_ms:,} ms, which is above the 5s threshold.",
        severity=InsightSeverity.warning,
        icon="🐢",
    )


def large_prompt_rule(trace: Trace, _: SessionStatistics | None = None) -> Insight | None:
    """Flag prompts that exceed the large-prompt threshold."""
    if trace.input_tokens <= LARGE_PROMPT_THRESHOLD_TOKENS:
        return None

    return Insight(
        title="Large Prompt",
        description=(
            f"Prompt size reached {trace.input_tokens:,} input tokens, which may affect cost and latency."
        ),
        severity=InsightSeverity.warning,
        icon="📦",
    )


def failed_request_rule(trace: Trace, _: SessionStatistics | None = None) -> Insight | None:
    """Flag terminal request failures."""
    if trace.status != "error":
        return None

    return Insight(
        title="Failed Request",
        description="The trace ended in an error state and should be investigated.",
        severity=InsightSeverity.critical,
        icon="⛔",
    )


def retry_detected_rule(trace: Trace, session_stats: SessionStatistics | None = None) -> Insight | None:
    """Flag traces that appear to be part of a retry flow."""
    prompt = trace.prompt.lower()
    response = trace.response.lower()
    operation = (session_stats.current_operation if session_stats else None) or ""
    flags = session_stats.flags if session_stats else ()

    retry_markers = (prompt, response, operation.lower(), *(flag.lower() for flag in flags))
    if not any("retry" in marker for marker in retry_markers):
        return None

    return Insight(
        title="Retry Detected",
        description="The trace or surrounding session context suggests a retry path.",
        severity=InsightSeverity.warning,
        icon="↻",
    )


def highest_cost_rule(trace: Trace, session_stats: SessionStatistics | None = None) -> Insight | None:
    """Flag the trace if it is the most expensive observed in the session."""
    if session_stats is None or session_stats.highest_cost_observed is None:
        return None

    if trace.cost < session_stats.highest_cost_observed:
        return None

    return Insight(
        title="Highest Cost",
        description=f"This trace is the most expensive observed so far at ${trace.cost:.4f}.",
        severity=InsightSeverity.info,
        icon="💸",
    )


DEFAULT_RULES: tuple[InsightRule, ...] = (
    slow_request_rule,
    large_prompt_rule,
    failed_request_rule,
    retry_detected_rule,
    highest_cost_rule,
)
