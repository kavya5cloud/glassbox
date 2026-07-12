from __future__ import annotations

import runpy
from pathlib import Path

from typer.testing import CliRunner

import glassbox.cli as cli


class DummyApp:
    runs: list[bool] = []

    def __init__(self, *, demo_mode: bool = False, **kwargs) -> None:
        self.demo_mode = demo_mode

    def run(self) -> None:
        DummyApp.runs.append(self.demo_mode)


def test_cli_without_subcommand_launches_normal_ui(monkeypatch) -> None:
    DummyApp.runs.clear()
    monkeypatch.setattr(cli, "GlassboxApp", DummyApp)

    result = CliRunner().invoke(cli.app, [])

    assert result.exit_code == 0
    assert DummyApp.runs == [False]


def test_cli_watch_command_launches_normal_ui(monkeypatch) -> None:
    DummyApp.runs.clear()
    monkeypatch.setattr(cli, "GlassboxApp", DummyApp)

    result = CliRunner().invoke(cli.app, ["watch"])

    assert result.exit_code == 0
    assert DummyApp.runs == [False]


def test_cli_demo_command_launches_demo_mode(monkeypatch) -> None:
    DummyApp.runs.clear()
    monkeypatch.setattr(cli, "GlassboxApp", DummyApp)

    result = CliRunner().invoke(cli.app, ["demo"])

    assert result.exit_code == 0
    assert DummyApp.runs == [True]


def test_cli_module_entrypoint_invokes_app(monkeypatch) -> None:
    calls: list[tuple[tuple, dict]] = []

    def fake_call(self, *args, **kwargs):
        calls.append((args, kwargs))

    monkeypatch.setattr("typer.main.Typer.__call__", fake_call)

    runpy.run_path(Path(cli.__file__), run_name="__main__")

    assert len(calls) == 1
    assert calls[0] == ((), {})
