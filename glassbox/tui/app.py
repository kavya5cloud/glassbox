from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from glassbox.tui.widgets import LiveTraceList


class GlassboxApp(App):

    CSS_PATH = "glassbox.tcss"

    TITLE = "Glassbox"

    def compose(self) -> ComposeResult:
        yield Header()
        yield LiveTraceList()
        yield Footer()