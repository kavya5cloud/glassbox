"""Textual widgets for the live trace experience."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from uuid import UUID

from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from textual.app import ComposeResult
from textual.containers import Container, Vertical, VerticalScroll
from textual.widgets import DataTable, Static

from glassbox.demo import DemoEngine, ScriptedTraceSource
from glassbox.insights import (
    Insight,
    InsightAnalyzer,
    InsightSeverity,
    SessionAnalyzer,
    SessionStatistics,
)
from glassbox.tracing import EventBus, Trace
from glassbox.tracing.bus import default_bus

TERMINAL_STATUSES = {"completed", "failed", "error"}
SLOW_LATENCY_MS = 3000
LARGE_PROMPT_TOKENS = 8000

PROVIDER_COLORS = {
    "OpenAI": "green",
    "Anthropic": "dark_orange",
    "Google": "blue",
    "Gemini": "blue",
}

STATUS_STYLES = {
    "running": "yellow",
    "updating": "yellow",
    "completed": "green",
    "failed": "red",
    "error": "red",
}

INSIGHT_SEVERITY_STYLES = {
    InsightSeverity.info: "cyan",
    InsightSeverity.warning: "yellow",
    InsightSeverity.critical: "red",
}


@dataclass(slots=True)
class TraceSummary:
    """Aggregated stats for the bottom status bar."""

    calls: int
    tokens: int
    spend: float
    errors: int
    mode: str


def _provider_style(provider: str) -> str:
    return PROVIDER_COLORS.get(provider, "cyan")


def _status_label(trace: Trace) -> tuple[str, str]:
    if trace.status in {"completed"}:
        return "Complete", "🟢"
    if trace.status in {"failed", "error"}:
        return "Error", "🔴"
    return "Running", "🟡"


def _trace_operation(trace: Trace) -> str:
    prompt = trace.prompt.strip()
    if ":" in prompt:
        prefix = prompt.split(":", 1)[0].strip()
        if 0 < len(prefix.split()) <= 4:
            return prefix
    return "LLM request"


def _trace_flags(trace: Trace) -> list[str]:
    flags: list[str] = []
    if trace.latency_ms >= SLOW_LATENCY_MS:
        flags.append("Slow")
    if trace.input_tokens >= LARGE_PROMPT_TOKENS:
        flags.append("Large prompt")
    prompt = trace.prompt.lower()
    if "retry" in prompt or trace.status in {"failed", "error"}:
        flags.append("Retry")
    return flags


def _token_count(trace: Trace) -> int:
    return trace.input_tokens + trace.output_tokens


def _compact_number(value: float | int) -> str:
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f}m"
    if value >= 1_000:
        return f"{value / 1_000:.1f}k"
    return f"{value:.0f}" if isinstance(value, int) else f"{value:.2f}"


def _meta_field(label: str, value: str, *, style: str = "white") -> Text:
    text = Text()
    text.append(f"{label}\n", style="dim")
    text.append(value or "—", style=style)
    return text


def _build_insight_card(insight: Insight) -> Panel:
    severity_style = INSIGHT_SEVERITY_STYLES.get(insight.severity, "cyan")
    body = Text()
    body.append(f"{insight.severity.value.capitalize()}\n", style=f"bold {severity_style}")
    body.append(insight.description, style="white")
    return Panel(
        body,
        title=f"{insight.icon} {insight.title}",
        border_style=severity_style,
        padding=(1, 1),
    )


def _build_insights_section(insights: list[Insight]) -> Group:
    if not insights:
        return Group(
            Panel(
                Text("No notable insights for this request.", style="dim"),
                border_style="grey30",
                padding=(1, 1),
            )
        )

    return Group(*(_build_insight_card(insight) for insight in insights))


def _format_latency(value_ms: float) -> str:
    if value_ms >= 1_000:
        return f"{value_ms / 1_000:.1f} s"
    return f"{value_ms:.0f} ms"


def _format_request_summary(trace: Trace) -> str:
    return f"{trace.provider} / {trace.model} • {trace.input_tokens:,} tokens"


def _build_summary_metric(label: str, value: str, *, style: str = "white") -> Text:
    text = Text()
    text.append(f"{label}\n", style="dim")
    text.append(value or "—", style=style)
    return text


def _build_session_summary_content(traces: list[Trace], session_stats: SessionStatistics, insights: list[Insight]) -> Group:
    total_requests = len(traces)
    largest_prompt = max(traces, key=lambda trace: trace.input_tokens, default=None)
    slowest_request = max(traces, key=lambda trace: trace.latency_ms, default=None)

    summary = Table.grid(expand=True, padding=(0, 1))
    summary.add_column(ratio=1)
    summary.add_column(ratio=1)
    summary.add_row(
        _build_summary_metric("Total Requests", f"{total_requests}", style="bold white"),
        _build_summary_metric("Average Latency", _format_latency(session_stats.average_latency_ms), style="cyan"),
    )
    summary.add_row(
        _build_summary_metric("Total Tokens", _compact_number(session_stats.total_input_tokens + session_stats.total_output_tokens), style="bold white"),
        _build_summary_metric("Total Spend", f"${session_stats.total_cost:.4f}", style="magenta"),
    )
    summary.add_row(
        _build_summary_metric(
            "Largest Prompt",
            "—" if largest_prompt is None else f"{largest_prompt.input_tokens:,} tokens • {_format_request_summary(largest_prompt)}",
            style="yellow",
        ),
        _build_summary_metric(
            "Slowest Request",
            "—" if slowest_request is None else f"{_format_latency(float(slowest_request.latency_ms))} • {_format_request_summary(slowest_request)}",
            style="red" if session_stats.slowest_latency_ms >= 5_000 else "white",
        ),
    )
    summary.add_row(
        _build_summary_metric("Retry Count", f"{session_stats.retry_count}", style="yellow" if session_stats.retry_count else "dim"),
        _build_summary_metric("Error Count", f"{session_stats.error_count}", style="red" if session_stats.error_count else "dim"),
    )

    return Group(
        Text("Session Summary", style="bold white"),
        Panel(summary, border_style="grey30", padding=(1, 1)),
        Text("Analysis", style="bold white"),
        _build_insights_section(insights)
        if insights
        else Panel(
            Text("No notable insights for this session.", style="dim"),
            border_style="grey30",
            padding=(1, 1),
        ),
    )


def _build_inspector_content(trace: Trace, insights: list[Insight]) -> Group:
    provider_style = _provider_style(trace.provider)
    tokens = _token_count(trace)
    status_label, status_icon = _status_label(trace)

    meta = Table.grid(expand=True, padding=(0, 1))
    meta.add_column(ratio=1)
    meta.add_column(ratio=1)
    meta.add_column(ratio=1)
    meta.add_row(
        _meta_field("Provider", trace.provider, style=provider_style),
        _meta_field("Model", trace.model, style="bold white"),
        _meta_field("Operation", _trace_operation(trace), style="bold white"),
    )
    meta.add_row(
        _meta_field("Latency", f"{trace.latency_ms:,} ms", style=STATUS_STYLES.get(trace.status, "cyan")),
        _meta_field("Tokens", f"{trace.input_tokens:,} in / {trace.output_tokens:,} out", style="cyan"),
        _meta_field("Estimated cost", f"${trace.cost:.4f}", style="magenta"),
    )

    prompt_text = Text(trace.prompt or "No prompt captured.", style="white", overflow="fold")
    response_text = Text(trace.response or "No response captured.", style="white", overflow="fold")

    prompt_panel = Panel(
        prompt_text,
        title="Prompt",
        border_style=provider_style,
        padding=(1, 1),
    )
    response_panel = Panel(
        response_text,
        title="Response",
        border_style="green",
        padding=(1, 1),
    )

    metadata = Table.grid(expand=True, padding=(0, 1))
    metadata.add_column(ratio=1)
    metadata.add_column(ratio=1)
    metadata.add_row(
        _meta_field("Status", f"{status_icon} {status_label}", style=STATUS_STYLES.get(trace.status, "cyan")),
        _meta_field("Total tokens", _compact_number(tokens), style="bold white"),
    )
    metadata.add_row(
        _meta_field("Started", trace.started_at.isoformat(), style="dim"),
        _meta_field("Ended", trace.ended_at.isoformat() if trace.ended_at else "Running", style="dim"),
    )

    return Group(
        meta,
        Text("Insights", style="bold white"),
        _build_insights_section(insights),
        prompt_panel,
        response_panel,
        Panel(metadata, title="Metadata", border_style="grey30", padding=(1, 1)),
    )


def _build_status_content(summary: TraceSummary) -> Text:
    text = Text()
    text.append("Calls ", style="dim")
    text.append(f"{summary.calls}", style="bold white")
    text.append("  ")
    text.append("Tokens ", style="dim")
    text.append(_compact_number(summary.tokens), style="bold white")
    text.append("  ")
    text.append("Spend ", style="dim")
    text.append(f"${summary.spend:.4f}", style="bold white")
    text.append("  ")
    text.append("Errors ", style="dim")
    text.append(f"{summary.errors}", style="bold red" if summary.errors else "bold white")
    text.append("  ")
    text.append("Mode ", style="dim")
    text.append(summary.mode, style="bold green" if summary.mode == "Demo" else "bold cyan")
    return text


class TraceFeed(DataTable):
    """Live-updating feed of trace events."""

    def __init__(self, bus: EventBus | None = None, *, max_rows: int = 80, name: str | None = None) -> None:
        super().__init__(name=name, zebra_stripes=False)
        self._bus = bus or default_bus
        self._max_rows = max_rows
        self._subscribed = False
        self._row_keys: list[object] = []
        self._trace_by_key: dict[object, Trace] = {}

    def on_mount(self) -> None:
        self.cursor_type = "row"
        self.show_header = True
        self.show_cursor = True
        self.add_columns("Status", "Provider", "Model", "Operation", "Latency", "Tokens", "Cost", "Flags")
        self.focus()
        if not self._subscribed:
            self._bus.subscribe(self._handle_trace)
            self._subscribed = True

    def _handle_trace(self, trace: Trace) -> None:
        self.call_from_thread(self.append_trace, trace)

    def append_trace(self, trace: Trace, *, select_row: bool = True) -> None:
        status_label, status_icon = _status_label(trace)
        provider = Text(trace.provider, style=_provider_style(trace.provider))
        model = Text(trace.model, style="bold white")
        operation = Text(_trace_operation(trace), style="white")
        latency_style = "red" if trace.latency_ms >= SLOW_LATENCY_MS else "white"
        token_style = "cyan" if trace.input_tokens >= LARGE_PROMPT_TOKENS else "white"
        flags = _trace_flags(trace)
        flags_text = Text(", ".join(flags) if flags else "—", style="yellow" if flags else "dim")
        status_text = Text(f"{status_icon} {status_label}", style=STATUS_STYLES.get(trace.status, "cyan"))
        latency = Text(f"{trace.latency_ms:,} ms", style=latency_style)
        tokens = Text(_compact_number(_token_count(trace)), style=token_style)
        cost = Text(f"${trace.cost:.4f}", style="magenta")

        row_key = self.add_row(
            status_text,
            provider,
            model,
            operation,
            latency,
            tokens,
            cost,
            flags_text,
            key=str(trace.id),
        )
        self._row_keys.append(row_key)
        self._trace_by_key[row_key] = trace

        while len(self._row_keys) > self._max_rows:
            old_key = self._row_keys.pop(0)
            self._trace_by_key.pop(old_key, None)
            try:
                self.remove_row(old_key)
            except Exception:
                break

        self.scroll_end(animate=False, immediate=True)
        if select_row and (len(self._row_keys) == 1 or trace.status in TERMINAL_STATUSES):
            self.move_cursor(row=self.row_count - 1)

    def latest_trace(self) -> Trace | None:
        if not self._row_keys:
            return None
        return self._trace_by_key.get(self._row_keys[-1])

    def trace_at_cursor(self) -> Trace | None:
        row_index = self.cursor_row
        if row_index is None or row_index < 0 or row_index >= len(self._row_keys):
            return None
        row_key = self._row_keys[row_index]
        return self._trace_by_key.get(row_key)

    def on_data_table_row_highlighted(self, event: DataTable.RowHighlighted) -> None:  # type: ignore[override]
        trace = self._trace_by_key.get(event.row_key)
        if trace is None:
            return
        dashboard = self.app.query_one(TraceDashboard)
        dashboard.focus_trace(trace)

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:  # type: ignore[override]
        trace = self._trace_by_key.get(event.row_key)
        if trace is None:
            return
        dashboard = self.app.query_one(TraceDashboard)
        dashboard.focus_trace(trace)


class TraceInspector(VerticalScroll):
    """Scrollable trace inspector with compact metadata and large detail panels."""

    def __init__(self, analyzer: InsightAnalyzer | None = None, *, name: str | None = None) -> None:
        super().__init__(name=name)
        self._analyzer = analyzer or InsightAnalyzer()
        self._session_analyzer = SessionAnalyzer()
        self._content = Static("", classes="trace-inspector-content")
        self._renderable: object | None = None
        self._mode = "request"

    def compose(self) -> ComposeResult:
        yield self._content

    def on_mount(self) -> None:
        self.show_trace(None)

    def show_trace(self, trace: Trace | None, session_stats: SessionStatistics | None = None) -> None:
        self._mode = "request"
        if trace is None:
            self._renderable = Panel(
                Text("Waiting for DemoEngine events...", style="dim"),
                title="Inspector",
                border_style="cyan",
                padding=(1, 1),
            )
            self._content.update(self._renderable)
            return

        insights = self._analyzer.analyze(trace, session_stats)
        self._renderable = _build_inspector_content(trace, insights)
        self._content.update(self._renderable)
        if self.is_mounted:
            self.scroll_home(animate=False, immediate=True)

    def show_session_summary(self, traces: list[Trace], session_stats: SessionStatistics | None = None) -> None:
        self._mode = "session"
        stats = session_stats or SessionStatistics()
        insights = self._session_analyzer.analyze(traces, stats)
        self._renderable = _build_session_summary_content(traces, stats, insights)
        self._content.update(self._renderable)
        if self.is_mounted:
            self.scroll_home(animate=False, immediate=True)

    @property
    def renderable_content(self) -> object | None:
        return self._renderable

    @property
    def mode(self) -> str:
        return self._mode


class TraceStatusBar(Static):
    """Bottom status strip for aggregate trace metrics."""

    def __init__(self, *, name: str | None = None) -> None:
        super().__init__("", name=name)

    def update_summary(self, summary: TraceSummary) -> None:
        self.update(_build_status_content(summary))


class TraceDashboard(Vertical):
    """Primary dashboard shell: title, feed, inspector, and status bar."""

    def __init__(
        self,
        bus: EventBus | None = None,
        *,
        demo_mode: bool = False,
        name: str | None = None,
    ) -> None:
        super().__init__(name=name, id="dashboard")
        self._bus = bus or (EventBus() if demo_mode else default_bus)
        self._demo_mode = demo_mode
        self._demo_task: asyncio.Task[None] | None = None
        self._traces: list[Trace] = []
        self._selected_trace_id: UUID | None = None
        self._session_mode = False
        self._feed: TraceFeed | None = None
        self._inspector: TraceInspector | None = None
        self._status_bar: TraceStatusBar | None = None

    def compose(self) -> ComposeResult:
        yield Static("Glassbox", id="titlebar")
        with Container(id="workspace"):
            with Vertical(id="feed-pane"):
                yield TraceFeed(bus=self._bus, id="trace-feed")
            with Vertical(id="inspector-pane"):
                yield TraceInspector(id="trace-inspector")
        yield TraceStatusBar(id="status-bar")

    def on_mount(self) -> None:
        self._feed = self.query_one("#trace-feed", TraceFeed)
        self._inspector = self.query_one("#trace-inspector", TraceInspector)
        self._status_bar = self.query_one("#status-bar", TraceStatusBar)
        self._bus.subscribe(self._handle_trace)
        self._refresh_summary()
        if self._feed is not None:
            self._feed.focus()
        if self._demo_mode:
            self._demo_task = asyncio.create_task(self._run_demo())

    def on_unmount(self) -> None:
        if self._demo_task is not None:
            self._demo_task.cancel()

    async def _run_demo(self) -> None:
        engine = DemoEngine(bus=self._bus, source=ScriptedTraceSource(), speed=1.0)
        try:
            await engine.run()
            self.show_session_summary()
        except asyncio.CancelledError:
            raise

    def _handle_trace(self, trace: Trace) -> None:
        self.call_from_thread(self._append_trace, trace)

    def _append_trace(self, trace: Trace) -> None:
        self._traces.append(trace)
        if self._feed is not None:
            self._feed.append_trace(trace, select_row=not self._session_mode)
        if not self._session_mode and (self._selected_trace_id is None or trace.status in TERMINAL_STATUSES):
            self.focus_trace(trace)
        elif self._session_mode:
            self.show_session_summary()
        self._refresh_summary()

    def _retry_like(self, trace: Trace) -> bool:
        prompt = trace.prompt.lower()
        response = trace.response.lower()
        return trace.status in {"failed", "error"} or "retry" in prompt or "retry" in response

    def _session_statistics(self, trace: Trace | None = None) -> SessionStatistics:
        total_input_tokens = sum(item.input_tokens for item in self._traces)
        total_output_tokens = sum(item.output_tokens for item in self._traces)
        total_cost = sum(item.cost for item in self._traces)
        average_latency_ms = (sum(item.latency_ms for item in self._traces) / len(self._traces)) if self._traces else 0.0
        highest_cost_observed = max((item.cost for item in self._traces), default=None)
        largest_prompt_tokens = max((item.input_tokens for item in self._traces), default=0)
        slowest_latency_ms = max((item.latency_ms for item in self._traces), default=0)
        retry_count = sum(1 for item in self._traces if self._retry_like(item))
        error_count = sum(1 for item in self._traces if item.status in {"failed", "error"})
        return SessionStatistics(
            trace_count=len(self._traces),
            total_input_tokens=total_input_tokens,
            total_output_tokens=total_output_tokens,
            total_cost=total_cost,
            average_latency_ms=average_latency_ms,
            retry_count=retry_count,
            error_count=error_count,
            largest_prompt_tokens=largest_prompt_tokens,
            slowest_latency_ms=slowest_latency_ms,
            highest_cost_observed=highest_cost_observed,
            current_operation=_trace_operation(trace) if trace is not None else None,
        )

    def focus_trace(self, trace: Trace) -> None:
        self._session_mode = False
        self._selected_trace_id = trace.id
        if self._inspector is not None:
            self._inspector.show_trace(trace, self._session_statistics(trace))

    def _current_trace(self) -> Trace | None:
        if self._selected_trace_id is not None:
            for trace in reversed(self._traces):
                if trace.id == self._selected_trace_id:
                    return trace
        if self._traces:
            return self._traces[-1]
        return None

    def show_session_summary(self, session_stats: SessionStatistics | None = None) -> None:
        self._session_mode = True
        if self._inspector is not None:
            self._inspector.show_session_summary(self._traces, session_stats or self._session_statistics())

    def show_request_inspector(self) -> None:
        trace = self._current_trace()
        if trace is not None:
            self.focus_trace(trace)

    def toggle_inspector_mode(self) -> None:
        if self._session_mode:
            self.show_request_inspector()
        else:
            self.show_session_summary()

    def on_key(self, event) -> None:  # type: ignore[override]
        if event.key == "tab":
            self.toggle_inspector_mode()
            event.stop()
        elif event.key == "s":
            self.show_session_summary()
            event.stop()
        elif event.key in {"r", "escape"}:
            self.show_request_inspector()
            event.stop()

    def _refresh_summary(self) -> None:
        if self._status_bar is None:
            return
        terminal_traces = [trace for trace in self._traces if trace.status in TERMINAL_STATUSES]
        summary = TraceSummary(
            calls=len(terminal_traces),
            tokens=sum(_token_count(trace) for trace in terminal_traces),
            spend=sum(trace.cost for trace in terminal_traces),
            errors=sum(1 for trace in terminal_traces if trace.status in {"failed", "error"}),
            mode="Demo" if self._demo_mode else "Live",
        )
        self._status_bar.update_summary(summary)


LiveTraceList = TraceDashboard
