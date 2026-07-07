from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

ASCII = r"""
 ███  █      ███   ████  ████ ████   ███  █   █
█ ░░░ █░    █ ░░█ █ ░░░░█ ░░░░█░░░█ █ ░░█  █ █ ░
█░ ██░█░░   █████░ ███░░░███░░████░░█░ ░█░  █ ░ ░
█░░ █░█░░   █░░░█░░ ░░█   ░░█ █░░░█ █░░ █░░█ █ ░
 ███ ░█████ █░░░█░████░░████░░████░░ ███ ░█ ░ █
"""

TEXT = f"""
{ASCII}

DevTools for LLM Applications

Inspect every prompt. Replay every run.

Open source • Local first • Zero telemetry

────────────────────────────────────────────

Waiting for AI traffic...

Run your application in another terminal.

glassbox watch
"""

class GlassboxApp(App):

    CSS_PATH = "glassbox.tcss"

    TITLE = "Glassbox"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(TEXT)
        yield Footer()