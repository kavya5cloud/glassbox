"""Minimal Textual application for the Glassbox core surfaces.

Public API:
- GlassboxApp

Future extension points:
- session browser
- evaluation panes
- plugin-aware views
"""

from __future__ import annotations

from typing import Any

from textual.app import App, ComposeResult
from textual.widgets import Static

from glassbox.evaluation import EvaluationRunner
from glassbox.sdk import Glassbox


class GlassboxApp(App[None]):
    """A small Textual app that renders core state."""

    CSS_PATH = "glassbox.tcss"
    TITLE = "Glassbox"
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("ctrl+c", "quit", "Quit"),
    ]

    def __init__(
        self,
        *,
        demo_mode: bool = False,
        sdk: Glassbox | None = None,
        evaluator: EvaluationRunner | None = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(**kwargs)
        self._demo_mode = demo_mode
        self._sdk = sdk or Glassbox.blank()
        self._evaluator = evaluator or EvaluationRunner()

    def compose(self) -> ComposeResult:
        session_id = self._sdk.session.id if self._sdk.session is not None else "idle"
        yield Static(
            "\n".join(
                [
                    "Glassbox Core",
                    f"Mode: {'demo' if self._demo_mode else 'live'}",
                    f"Session: {session_id}",
                    f"Identity: {self._sdk.identity.digest}",
                    f"Scorer: {self._evaluator.scorer.__class__.__name__}",
                ]
            ),
            id="glassbox-core",
        )
