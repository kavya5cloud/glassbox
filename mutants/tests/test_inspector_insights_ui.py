from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.console import Group

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


def render_text(renderable) -> str:
    console = Console(record=True, width=100)
    console.print(renderable)
    return console.export_text(clear=False)


def collect_panels(renderable) -> list[Panel]:
    panels: list[Panel] = []
    if isinstance(renderable, Panel):
        panels.append(renderable)
        inner = renderable.renderable
        panels.extend(collect_panels(inner))
    elif isinstance(renderable, Group):
        for item in renderable.renderables:
            panels.extend(collect_panels(item))
    return panels


def insight_titles(renderable) -> list[str]:
    return [panel.title for panel in collect_panels(renderable) if panel.title and panel.title != "Metadata"]


def insight_panel_for(renderable, title_fragment: str) -> Panel | None:
    for panel in collect_panels(renderable):
        title = panel.title or ""
        if title_fragment in title:
            return panel
    return None


def test_slow_request_renders_insight_card() -> None:
    inspector = TraceInspector()
    trace = make_trace(latency_ms=5_001)

    inspector.show_trace(trace, SessionStatistics(highest_cost_observed=trace.cost))

    text = render_text(inspector.renderable_content)
    assert "Slow Request" in text
    panel = insight_panel_for(inspector.renderable_content, "Slow Request")
    assert panel is not None
    assert panel.border_style == "yellow"


def test_large_prompt_renders_insight_card() -> None:
    inspector = TraceInspector()
    trace = make_trace(input_tokens=10_001)

    inspector.show_trace(trace, SessionStatistics(highest_cost_observed=trace.cost))

    text = render_text(inspector.renderable_content)
    assert "Large Prompt" in text
    panel = insight_panel_for(inspector.renderable_content, "Large Prompt")
    assert panel is not None
    assert panel.border_style == "yellow"


def test_failed_request_renders_insight_card() -> None:
    inspector = TraceInspector()
    trace = make_trace(status="error")

    inspector.show_trace(trace, SessionStatistics(highest_cost_observed=trace.cost))

    text = render_text(inspector.renderable_content)
    assert "Failed Request" in text
    panel = insight_panel_for(inspector.renderable_content, "Failed Request")
    assert panel is not None
    assert panel.border_style == "red"


def test_retry_renders_insight_card() -> None:
    inspector = TraceInspector()
    trace = make_trace()
    stats = SessionStatistics(current_operation="retry payment verification")

    inspector.show_trace(trace, stats)

    text = render_text(inspector.renderable_content)
    assert "Retry Detected" in text
    panel = insight_panel_for(inspector.renderable_content, "Retry Detected")
    assert panel is not None
    assert panel.border_style == "yellow"


def test_highest_cost_renders_insight_card() -> None:
    inspector = TraceInspector()
    trace = make_trace(cost=0.0314)
    stats = SessionStatistics(highest_cost_observed=0.0314)

    inspector.show_trace(trace, stats)

    text = render_text(inspector.renderable_content)
    assert "Highest Cost" in text
    panel = insight_panel_for(inspector.renderable_content, "Highest Cost")
    assert panel is not None
    assert panel.border_style == "cyan"


def test_empty_state_renders_subdued_message() -> None:
    inspector = TraceInspector()
    trace = make_trace()

    inspector.show_trace(trace, SessionStatistics(highest_cost_observed=trace.cost + 0.001))

    text = render_text(inspector.renderable_content)
    assert "No notable insights for this request." in text
