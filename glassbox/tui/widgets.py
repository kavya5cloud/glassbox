"""Textual widgets for the live trace experience."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import DataTable, Static

from glassbox.tracing import DemoTraceSource, EventBus, Trace
from glassbox.tracing.bus import default_bus
from glassbox.tui.screens import TraceInspectorScreen


class LiveTraceList(Container):
    """A live-updating table of the most recent traces."""

    def __init__(self, bus: EventBus | None = None, *, name: str | None = None) -> None:
        super().__init__(name=name)
        self._bus = bus or default_bus
        self._traces: list[Trace] = []
        self._table = DataTable(zebra_stripes=True)
        self._generator: DemoTraceSource | None = None
        self._subscribed = False

    def compose(self) -> ComposeResult:
        yield self._table
        yield Static("Waiting for traces...", classes="trace-status")

    def on_mount(self) -> None:
        self._table.add_columns("Provider", "Model", "Cost", "Latency")
        self._table.cursor_type = "row"
        self._table.show_header = True
        self._table.focus()
        if not self._subscribed:
            self._bus.subscribe(self._handle_trace)
            self._subscribed = True
        self._generator = DemoTraceSource(self._bus)
        self._generator.start()
        self._refresh_rows()

    def _handle_trace(self, trace: Trace) -> None:
        self.call_from_thread(self._append_trace, trace)

    def _append_trace(self, trace: Trace) -> None:
        self._traces.insert(0, trace)
        self._traces = self._traces[:50]
        self.call_after_refresh(self._refresh_rows)

    def _refresh_rows(self) -> None:
        if not self.is_mounted:
            return

        self._table.clear(columns=True)
        self._table.add_columns("Provider", "Model", "Cost", "Latency")
        for trace in self._traces:
            self._table.add_row(
                trace.provider,
                trace.model,
                f"${trace.cost:.3f}",
                f"{trace.latency_ms} ms",
            )
        if self._traces:
            self._table.move_cursor(row=0)

    def on_key(self, event) -> None:
        if event.key == "enter":
            row_index = self._table.cursor_row
            if row_index is None or row_index >= len(self._traces):
                return
            trace = self._traces[row_index]
            self.app.push_screen(TraceInspectorScreen(trace))
            event.stop()
