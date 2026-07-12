from __future__ import annotations

from typing import Any

from textual.app import App, ComposeResult

from glassbox.tui.widgets import TraceDashboard


class GlassboxApp(App):

    CSS_PATH = "glassbox.tcss"

    TITLE = "Glassbox"

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    def __init__(self, *, demo_mode: bool = False, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._demo_mode = demo_mode

    def compose(self) -> ComposeResult:
        yield TraceDashboard(demo_mode=self._demo_mode)

    def on_mount(self) -> None:
        self.set_class(self.size.width < 140, "compact")

    def on_resize(self, event: Any) -> None:
        self.set_class(event.size.width < 140, "compact")
