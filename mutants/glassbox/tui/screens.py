"""Textual screens for inspecting traced requests."""

from __future__ import annotations

from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Static

from glassbox.tracing import Trace


class TraceInspectorScreen(Screen[None]):
    """Display the full contents of a single trace."""

    def __init__(self, trace: Trace, *, name: str | None = None) -> None:
        super().__init__(name=name)
        self.trace = trace
        self._details = Static("", classes="trace-details")

    def compose(self) -> ComposeResult:
        yield Container(
            Static("Trace Inspector", classes="trace-title"),
            self._details,
            id="trace-inspector",
        )

    def on_mount(self) -> None:
        self._details.update(self._format_trace())

    def on_key(self, event) -> None:  # type: ignore[override]
        if event.key == "escape":
            self.app.pop_screen()
            event.stop()

    def _format_trace(self) -> str:
        return "\n".join(
            [
                f"Provider: {self.trace.provider}",
                f"Model: {self.trace.model}",
                f"Input Tokens: {self.trace.input_tokens}",
                f"Output Tokens: {self.trace.output_tokens}",
                f"Latency: {self.trace.latency_ms} ms",
                f"Cost: ${self.trace.cost:.3f}",
                f"Prompt: {self.trace.prompt}",
                f"Response: {self.trace.response}",
            ]
        )
