"""Session-level insight rules for summary analysis."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from statistics import mean

from glassbox.tracing import Trace

from .models import Insight, InsightSeverity, SessionStatistics

SessionInsightRule = Callable[[Sequence[Trace], SessionStatistics | None], Insight | None]

LARGE_CONTEXT_THRESHOLD_TOKENS = 10_000
SLOW_REQUEST_THRESHOLD_MS = 5_000
SIGNIFICANT_SPEND_SHARE = 0.25
PROMPT_GROWTH_DELTA = 0.15


def _retry_like(trace: Trace) -> bool:
    prompt = trace.prompt.lower()
    response = trace.response.lower()
    return trace.status in {"failed", "error"} or "retry" in prompt or "retry" in response


def _format_count(count: int, noun: str) -> str:
    suffix = noun if count == 1 else f"{noun}s"
    return f"{count} {suffix}"


def large_context_rule(traces: Sequence[Trace], _: SessionStatistics | None = None) -> Insight | None:
    large_context_traces = [trace for trace in traces if trace.input_tokens > LARGE_CONTEXT_THRESHOLD_TOKENS]
    if not large_context_traces:
        return None

    count = len(large_context_traces)
    return Insight(
        title="Large Context",
        description=f"Large context detected in {_format_count(count, 'request')}.",
        severity=InsightSeverity.warning,
        icon="⚠",
    )


def slow_request_volume_rule(traces: Sequence[Trace], _: SessionStatistics | None = None) -> Insight | None:
    slow_traces = [trace for trace in traces if trace.latency_ms > SLOW_REQUEST_THRESHOLD_MS]
    if not slow_traces:
        return None

    count = len(slow_traces)
    return Insight(
        title="Slow Requests",
        description=f"{_format_count(count, 'request')} exceeded 5 seconds.",
        severity=InsightSeverity.warning,
        icon="🐢",
    )


def spend_concentration_rule(traces: Sequence[Trace], session_stats: SessionStatistics | None = None) -> Insight | None:
    total_cost = (session_stats.total_cost if session_stats else 0.0) or sum(trace.cost for trace in traces)
    if total_cost <= 0:
        return None

    highest_cost = max((trace.cost for trace in traces), default=0.0)
    share = highest_cost / total_cost if total_cost else 0.0
    if share < SIGNIFICANT_SPEND_SHARE:
        return None

    return Insight(
        title="Spend Concentration",
        description=f"One request accounted for {share:.0%} of total spend.",
        severity=InsightSeverity.info,
        icon="💸",
    )


def retry_volume_rule(traces: Sequence[Trace], _: SessionStatistics | None = None) -> Insight | None:
    count = sum(1 for trace in traces if _retry_like(trace))
    if count == 0:
        return None

    return Insight(
        title="Retries",
        description=f"{count} {'retries' if count != 1 else 'retry'} detected.",
        severity=InsightSeverity.warning,
        icon="🔁",
    )


def prompt_growth_rule(traces: Sequence[Trace], _: SessionStatistics | None = None) -> Insight | None:
    if len(traces) < 4:
        return None

    midpoint = max(1, len(traces) // 2)
    first_half = [trace.input_tokens for trace in traces[:midpoint]]
    second_half = [trace.input_tokens for trace in traces[midpoint:]]
    if not first_half or not second_half:
        return None

    first_avg = mean(first_half)
    second_avg = mean(second_half)
    if second_avg <= first_avg * (1 + PROMPT_GROWTH_DELTA):
        return None

    return Insight(
        title="Prompt Growth",
        description="Average prompt size increased during the session.",
        severity=InsightSeverity.info,
        icon="📈",
    )


DEFAULT_SESSION_RULES = (
    large_context_rule,
    slow_request_volume_rule,
    spend_concentration_rule,
    retry_volume_rule,
    prompt_growth_rule,
)
