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


def _build_inspector_content(trace: Trace) -> Group:
    status_label, status_icon = _status_label(trace)
    provider_style = _provider_style(trace.provider)
    flags = _trace_flags(trace)
    tokens = _token_count(trace)

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
    meta.add_row(
        _meta_field("Status", f"{status_icon} {status_label}", style=STATUS_STYLES.get(trace.status, "cyan")),
        _meta_field("Total tokens", _compact_number(tokens), style="bold white"),
        _meta_field("Flags", ", ".join(flags) if flags else "None", style="yellow" if flags else "dim"),
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

    insights_lines = [
        f"{status_icon} {status_label} trace from {trace.provider} / {trace.model}",
    ]
    if trace.latency_ms >= SLOW_LATENCY_MS:
        insights_lines.append(f"Slow request: {trace.latency_ms:,} ms latency.")
    if trace.input_tokens >= LARGE_PROMPT_TOKENS:
        insights_lines.append(f"Large prompt: {trace.input_tokens:,} input tokens.")
    if "retry" in trace.prompt.lower() or trace.status in {"failed", "error"}:
        insights_lines.append("Retry path detected.")
    if trace.status in {"failed", "error"}:
        insights_lines.append("Terminal error state captured in the feed.")
    if len(insights_lines) == 1:
        insights_lines.append("No notable flags on this trace.")

    insights_panel = Panel(
        Text("\n".join(insights_lines), style="white", overflow="fold"),
        title="Insights",
        border_style="yellow",
        padding=(1, 1),
    )

    return Group(meta, prompt_panel, response_panel, insights_panel)


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

    def append_trace(self, trace: Trace) -> None:
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
        if len(self._row_keys) == 1 or trace.status in TERMINAL_STATUSES:
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

    def __init__(self, *, name: str | None = None) -> None:
        super().__init__(name=name)
        self._content = Static("", classes="trace-inspector-content")

    def compose(self) -> ComposeResult:
        yield self._content

    def on_mount(self) -> None:
        self.show_trace(None)

    def show_trace(self, trace: Trace | None) -> None:
        if trace is None:
            self._content.update(
                Panel(
                    Text("Waiting for DemoEngine events...", style="dim"),
                    title="Inspector",
                    border_style="cyan",
                    padding=(1, 1),
                )
            )
            return

        self._content.update(_build_inspector_content(trace))
        self.scroll_home(animate=False, immediate=True)


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
        except asyncio.CancelledError:
            raise

    def _handle_trace(self, trace: Trace) -> None:
        self.call_from_thread(self._append_trace, trace)

    def _append_trace(self, trace: Trace) -> None:
        self._traces.append(trace)
        if self._feed is not None:
            self._feed.append_trace(trace)
        if self._selected_trace_id is None or trace.status in TERMINAL_STATUSES:
            self.focus_trace(trace)
        self._refresh_summary()

    def focus_trace(self, trace: Trace) -> None:
        self._selected_trace_id = trace.id
        if self._inspector is not None:
            self._inspector.show_trace(trace)

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
