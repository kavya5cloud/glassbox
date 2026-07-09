from glassbox.insights import InsightAnalyzer, InsightSeverity, SessionStatistics
from glassbox.tracing import Trace


def make_trace(**overrides) -> Trace:
    base = dict(
        provider="OpenAI",
        model="gpt-5.5",
        input_tokens=1_000,
        output_tokens=250,
        latency_ms=1_000,
        cost=0.005,
        status="completed",
        prompt="Normal request",
        response="All good",
    )
    base.update(overrides)
    return Trace(**base)


def test_slow_request_rule_emits_warning_insight() -> None:
    analyzer = InsightAnalyzer()
    trace = make_trace(latency_ms=5_001)

    insights = analyzer.analyze(trace)

    assert len(insights) == 1
    assert insights[0].title == "Slow Request"
    assert insights[0].severity == InsightSeverity.warning
    assert insights[0].icon == "🐢"


def test_large_prompt_rule_emits_warning_insight() -> None:
    analyzer = InsightAnalyzer()
    trace = make_trace(input_tokens=10_001)

    insights = analyzer.analyze(trace)

    assert len(insights) == 1
    assert insights[0].title == "Large Prompt"
    assert insights[0].severity == InsightSeverity.warning
    assert insights[0].icon == "📦"


def test_failed_request_rule_emits_critical_insight() -> None:
    analyzer = InsightAnalyzer()
    trace = make_trace(status="error")

    insights = analyzer.analyze(trace)

    assert len(insights) == 1
    assert insights[0].title == "Failed Request"
    assert insights[0].severity == InsightSeverity.critical
    assert insights[0].icon == "⛔"


def test_retry_detected_rule_uses_session_operation_or_flags() -> None:
    analyzer = InsightAnalyzer()
    trace = make_trace()
    stats = SessionStatistics(current_operation="retry payment verification")

    insights = analyzer.analyze(trace, stats)

    assert len(insights) == 1
    assert insights[0].title == "Retry Detected"
    assert insights[0].severity == InsightSeverity.warning
    assert insights[0].icon == "↻"


def test_highest_cost_rule_emits_info_insight_for_session_high() -> None:
    analyzer = InsightAnalyzer()
    trace = make_trace(cost=0.0314)
    stats = SessionStatistics(highest_cost_observed=0.0314)

    insights = analyzer.analyze(trace, stats)

    assert len(insights) == 1
    assert insights[0].title == "Highest Cost"
    assert insights[0].severity == InsightSeverity.info
    assert insights[0].icon == "💸"

