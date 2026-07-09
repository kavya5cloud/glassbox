from __future__ import annotations

from rich.console import Console
from rich.console import Group
from rich.panel import Panel

from glassbox.insights import SessionStatistics
from glassbox.tui.widgets import TraceInspector
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


def build_stats(traces: list[Trace]) -> SessionStatistics:
    total_input_tokens = sum(trace.input_tokens for trace in traces)
    total_output_tokens = sum(trace.output_tokens for trace in traces)
    total_cost = sum(trace.cost for trace in traces)
    average_latency_ms = (sum(trace.latency_ms for trace in traces) / len(traces)) if traces else 0.0
    highest_cost_observed = max((trace.cost for trace in traces), default=None)
    largest_prompt_tokens = max((trace.input_tokens for trace in traces), default=0)
    slowest_latency_ms = max((trace.latency_ms for trace in traces), default=0)
    retry_count = sum(1 for trace in traces if trace.status in {"failed", "error"} or "retry" in trace.prompt.lower())
    error_count = sum(1 for trace in traces if trace.status in {"failed", "error"})
    return SessionStatistics(
        trace_count=len(traces),
        total_input_tokens=total_input_tokens,
        total_output_tokens=total_output_tokens,
        total_cost=total_cost,
        average_latency_ms=average_latency_ms,
        retry_count=retry_count,
        error_count=error_count,
        largest_prompt_tokens=largest_prompt_tokens,
        slowest_latency_ms=slowest_latency_ms,
        highest_cost_observed=highest_cost_observed,
    )


def render_text(renderable) -> str:
    console = Console(record=True, width=120)
    console.print(renderable)
    return console.export_text(clear=False)


def collect_panels(renderable) -> list[Panel]:
    panels: list[Panel] = []
    if isinstance(renderable, Panel):
        panels.append(renderable)
        panels.extend(collect_panels(renderable.renderable))
    elif isinstance(renderable, Group):
        for item in renderable.renderables:
            panels.extend(collect_panels(item))
    return panels


def insight_panel_for(renderable, title_fragment: str) -> Panel | None:
    for panel in collect_panels(renderable):
        title = panel.title or ""
        if title_fragment in title:
            return panel
    return None


def make_session_traces() -> list[Trace]:
    return [
        make_trace(prompt="Warmup request", input_tokens=1200, latency_ms=420, cost=0.0035),
        make_trace(prompt="Follow-up request", input_tokens=1400, latency_ms=560, cost=0.0041),
        make_trace(prompt="Baseline request", input_tokens=1500, latency_ms=920, cost=0.0068),
        make_trace(prompt="Retry request: payment verification", input_tokens=1800, latency_ms=6100, cost=0.0082, status="failed"),
        make_trace(prompt="Another large context", input_tokens=18_000, latency_ms=740, cost=0.0056),
        make_trace(prompt="Final retry attempt", input_tokens=25_000, latency_ms=830, cost=0.0210),
    ]


def test_session_summary_renders_metrics_and_analysis_cards() -> None:
    inspector = TraceInspector()
    traces = make_session_traces()
    stats = build_stats(traces)

    inspector.show_session_summary(traces, stats)

    text = render_text(inspector.renderable_content)
    assert "Session Summary" in text
    assert "Total Requests" in text
    assert "Average Latency" in text
    assert "Total Tokens" in text
    assert "Total Spend" in text
    assert "Largest Prompt" in text
    assert "Slowest Request" in text
    assert "Retry Count" in text
    assert "Error Count" in text
    assert "Analysis" in text

    large_context = insight_panel_for(inspector.renderable_content, "Large Context")
    slow_requests = insight_panel_for(inspector.renderable_content, "Slow Requests")
    spend = insight_panel_for(inspector.renderable_content, "Spend Concentration")
    retries = insight_panel_for(inspector.renderable_content, "Retries")
    growth = insight_panel_for(inspector.renderable_content, "Prompt Growth")

    assert large_context is not None
    assert slow_requests is not None
    assert spend is not None
    assert retries is not None
    assert growth is not None
    assert large_context.border_style == "yellow"
    assert slow_requests.border_style == "yellow"
    assert spend.border_style == "cyan"
    assert retries.border_style == "yellow"
    assert growth.border_style == "cyan"


def test_session_summary_empty_state_is_subdued() -> None:
    inspector = TraceInspector()

    inspector.show_session_summary([], SessionStatistics())

    text = render_text(inspector.renderable_content)
    assert "Session Summary" in text
    assert "No notable insights for this session." in text
