"""Glassbox command line interface.

Public API:
- app
- main

Future extension points:
- project discovery
- transport wiring
- export pipelines
"""

from __future__ import annotations

import json
import os
import subprocess
import tempfile
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast
from uuid import uuid4

import typer

from glassbox.core import Execution, Session
from glassbox.evaluation import EvaluationRunner
from glassbox.evaluation.diff import diff_datasets
from glassbox.storage import Dataset
from glassbox.tui.app import GlassboxApp

app = typer.Typer(help="Glassbox command line interface", invoke_without_command=True)


def _workspace_root(root: Path | None = None) -> Path:
    return root or Path(".glassbox")


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def _session_dir(session_id: str, root: Path | None = None) -> Path:
    return _workspace_root(root) / "sessions" / session_id


def _dataset_dir(dataset_id: str, root: Path | None = None) -> Path:
    return _workspace_root(root) / "datasets" / dataset_id


def _session_path(ref: str, root: Path | None = None) -> Path:
    candidate = Path(ref)
    if candidate.exists():
        if candidate.is_dir():
            return candidate
        return candidate.parent
    return _session_dir(ref, root)


def _dataset_path(ref: str, root: Path | None = None) -> Path:
    candidate = Path(ref)
    if candidate.exists():
        if candidate.is_dir():
            return candidate
        return candidate.parent
    return _dataset_dir(ref, root)


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    _ensure_dir(path.parent)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _serialize_session(session: Session) -> dict[str, Any]:
    return {
        **asdict(session),
        "started_at": session.started_at.isoformat(),
        "ended_at": session.ended_at.isoformat() if session.ended_at is not None else None,
    }


def _serialize_execution(execution: Execution) -> dict[str, Any]:
    return {
        **asdict(execution),
        "started_at": execution.started_at.isoformat(),
        "ended_at": execution.ended_at.isoformat() if execution.ended_at is not None else None,
    }


def _serialize_dataset(dataset: Dataset) -> dict[str, Any]:
    return {
        **asdict(dataset),
        "created_at": dataset.created_at.isoformat(),
    }


def _load_session(path: Path) -> Session:
    payload = _read_json(path / "session.json" if path.is_dir() else path)
    return Session(
        id=payload["id"],
        identity_ref=payload["identity_ref"],
        started_at=datetime.fromisoformat(payload["started_at"]),
        state=payload["state"],
        run_ids=tuple(payload.get("run_ids", ())),
        observation_ids=tuple(payload.get("observation_ids", ())),
        artifact_ids=tuple(payload.get("artifact_ids", ())),
        parent_session_id=payload.get("parent_session_id"),
        metadata=tuple(tuple(pair) for pair in payload.get("metadata", ())),
        ended_at=(
            datetime.fromisoformat(payload["ended_at"])
            if payload.get("ended_at") is not None
            else None
        ),
    )


def _load_execution(path: Path) -> Execution:
    payload = _read_json(path / "execution.json" if path.is_dir() else path)
    return Execution(
        id=payload["id"],
        session_id=payload["session_id"],
        identity_ref=payload["identity_ref"],
        state=payload["state"],
        started_at=datetime.fromisoformat(payload["started_at"]),
        ended_at=(
            datetime.fromisoformat(payload["ended_at"])
            if payload.get("ended_at") is not None
            else None
        ),
        observation_ids=tuple(payload.get("observation_ids", ())),
        artifact_ids=tuple(payload.get("artifact_ids", ())),
        parent_execution_id=payload.get("parent_execution_id"),
        metadata=tuple(tuple(pair) for pair in payload.get("metadata", ())),
    )


def _load_dataset(ref: str, root: Path | None = None) -> Dataset:
    path = _dataset_path(ref, root)
    payload_path = path / "dataset.json" if path.is_dir() else path
    if payload_path.exists():
        payload = _read_json(payload_path)
        return Dataset(
            id=payload["id"],
            name=payload["name"],
            session_ids=tuple(payload.get("session_ids", ())),
            observation_ids=tuple(payload.get("observation_ids", ())),
            artifact_ids=tuple(payload.get("artifact_ids", ())),
            created_at=datetime.fromisoformat(payload["created_at"]),
            metadata=tuple(tuple(pair) for pair in payload.get("metadata", ())),
        )

    execution = _load_execution(_session_path(ref, root))
    return Dataset(
        id=execution.id,
        name=f"execution:{execution.id}",
        session_ids=(execution.session_id,),
        observation_ids=execution.observation_ids,
        artifact_ids=execution.artifact_ids,
        metadata=execution.metadata,
    )


def _print_json(payload: dict[str, Any]) -> None:
    typer.echo(json.dumps(payload, indent=2, sort_keys=True))


def _format_duration(duration_seconds: float) -> str:
    return f"{duration_seconds:.3f}s"


def _lifecycle_observation(
    *,
    observation_id: str,
    session_id: str,
    execution_id: str,
    kind: str,
    occurred_at: datetime,
    command: list[str],
    cwd: str,
    pid: int | None = None,
    exit_code: int | None = None,
    duration_seconds: float | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "id": observation_id,
        "session_id": session_id,
        "execution_id": execution_id,
        "kind": kind,
        "occurred_at": occurred_at.isoformat(),
        "command": command,
        "cwd": cwd,
    }
    if pid is not None:
        payload["pid"] = pid
    if exit_code is not None:
        payload["exit_code"] = exit_code
    if duration_seconds is not None:
        payload["duration_seconds"] = duration_seconds
    return payload


def _capture_record(
    *,
    session_id: str,
    execution_id: str,
    started_at: datetime,
    ended_at: datetime,
    command: list[str],
    cwd: str,
    exit_code: int,
    observation_ids: tuple[str, ...],
) -> dict[str, Any]:
    duration_seconds = (ended_at - started_at).total_seconds()
    return {
        "session": {
            "id": session_id,
            "state": "complete" if exit_code == 0 else "failed",
            "started_at": started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "duration_seconds": duration_seconds,
            "command": command,
            "cwd": cwd,
            "observation_ids": list(observation_ids),
            "artifact_ids": [],
        },
        "execution": {
            "id": execution_id,
            "session_id": session_id,
            "state": "complete" if exit_code == 0 else "failed",
            "started_at": started_at.isoformat(),
            "ended_at": ended_at.isoformat(),
            "duration_seconds": duration_seconds,
            "exit_code": exit_code,
            "command": command,
            "cwd": cwd,
            "observation_ids": list(observation_ids),
            "artifact_ids": [],
        },
        "duration_seconds": duration_seconds,
    }


def _prepare_child_environment(
    *,
    session_id: str,
    execution_id: str,
    observations_path: Path,
) -> tuple[dict[str, str], tempfile.TemporaryDirectory[str]]:
    bootstrap = tempfile.TemporaryDirectory(prefix="glassbox-capture-")
    bootstrap_dir = Path(bootstrap.name)
    (bootstrap_dir / "sitecustomize.py").write_text(
        "from glassbox.capture.http import install_http_capture\n"
        "install_http_capture()\n",
        encoding="utf-8",
    )
    env = dict(os.environ)
    env["GLASSBOX_SESSION_ID"] = session_id
    env["GLASSBOX_EXECUTION_ID"] = execution_id
    env["GLASSBOX_OBSERVATIONS_PATH"] = str(observations_path)
    env["PYTHONPATH"] = (
        f"{bootstrap_dir}{os.pathsep}{env['PYTHONPATH']}" if env.get("PYTHONPATH") else str(bootstrap_dir)
    )
    return env, bootstrap


def _read_observation_ids(path: Path) -> tuple[str, ...]:
    observation_ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        observation_ids.append(cast(dict[str, Any], json.loads(line))["id"])
    return tuple(observation_ids)


@app.callback()
def main(ctx: typer.Context) -> None:
    """Run the default command when no subcommand is provided."""

    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())


@app.command()
def capture(
    command: list[str] = typer.Argument(
        ...,
        help="Command to execute under capture.",
    ),
) -> None:
    """Execute a Python program and record its session lifecycle."""

    cwd = Path.cwd()
    resolved_root = _workspace_root()
    session_id = f"session-{uuid4().hex[:12]}"
    execution_id = f"execution-{uuid4().hex[:12]}"
    session = Session.open(session_id, "capture")
    execution = Execution.running(id=execution_id, session_id=session.id, identity_ref="capture")

    session_dir = _ensure_dir(_session_dir(session.id, resolved_root))
    observations_path = session_dir / "observations.jsonl"
    child_env, bootstrap = _prepare_child_environment(
        session_id=session.id,
        execution_id=execution.id,
        observations_path=observations_path,
    )
    started_at = _utc_now()
    started_observation = _lifecycle_observation(
        observation_id=f"observation-{uuid4().hex[:12]}",
        session_id=session.id,
        execution_id=execution.id,
        kind="process_started",
        occurred_at=started_at,
        command=command,
        cwd=str(cwd),
        pid=None,
    )
    _write_json(
        session_dir / "session.json",
        {
            **_serialize_session(session),
            "command": command,
            "cwd": str(cwd),
            "started_at": started_at.isoformat(),
            "state": "running",
            "observation_ids": [started_observation["id"]],
            "artifact_ids": [],
        },
    )
    _write_json(
        session_dir / "execution.json",
        {
            **_serialize_execution(execution),
            "command": command,
            "cwd": str(cwd),
            "started_at": started_at.isoformat(),
            "state": "running",
            "exit_code": None,
        },
    )
    observations_path.write_text(json.dumps(started_observation, sort_keys=True) + "\n", encoding="utf-8")

    exit_code = 0
    ended_at = started_at
    try:
        try:
            completed = subprocess.run(command, cwd=str(cwd), env=child_env, check=False)
            exit_code = completed.returncode
            ended_at = _utc_now()
        except Exception:  # pragma: no cover - exercised by subprocess failures in CI
            exit_code = 1
            ended_at = _utc_now()

        finished_observation = _lifecycle_observation(
            observation_id=f"observation-{uuid4().hex[:12]}",
            session_id=session.id,
            execution_id=execution.id,
            kind="process_finished",
            occurred_at=ended_at,
            command=command,
            cwd=str(cwd),
            exit_code=exit_code,
            duration_seconds=(ended_at - started_at).total_seconds(),
        )
        with observations_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(finished_observation, sort_keys=True) + "\n")

        observation_ids = _read_observation_ids(observations_path)
        record = _capture_record(
            session_id=session.id,
            execution_id=execution.id,
            started_at=started_at,
            ended_at=ended_at,
            command=command,
            cwd=str(cwd),
            exit_code=exit_code,
            observation_ids=observation_ids,
        )
        _write_json(
            session_dir / "session.json",
            {
                **record["session"],
                "identity_ref": session.identity_ref,
                "run_ids": [execution.id],
                "parent_session_id": None,
                "metadata": (),
            },
        )
        _write_json(
            session_dir / "execution.json",
            {
                **record["execution"],
                "identity_ref": execution.identity_ref,
                "parent_execution_id": None,
                "metadata": (),
            },
        )
    finally:
        bootstrap.cleanup()

    typer.echo(f"Session created:\n{session.id}")
    typer.echo()
    typer.echo(f"Duration:\n{_format_duration(record['duration_seconds'])}")
    typer.echo()
    typer.echo("Observations:")
    typer.echo(str(len(observation_ids)))
    typer.echo()
    typer.echo("Artifacts:")
    typer.echo("0")

    if exit_code != 0:
        raise typer.Exit(code=exit_code)


@app.command()
def dataset(
    session: str = typer.Argument(..., help="Session id or session directory."),
    name: str | None = typer.Option(None, "--name", help="Dataset name."),
    dataset_id: str | None = typer.Option(None, "--dataset-id", help="Override the dataset id."),
    root: Path = typer.Option(
        Path(".glassbox"),
        "--root",
        help="Workspace root used to store dataset artifacts.",
        dir_okay=True,
        file_okay=False,
        exists=False,
        resolve_path=False,
    ),
) -> None:
    """Create a dataset snapshot from an existing session."""

    resolved_root = _workspace_root(root)
    session_record = _load_session(_session_path(session, resolved_root))
    execution_record = _load_execution(_session_path(session, resolved_root))
    dataset = Dataset(
        id=dataset_id or f"dataset-{session_record.id}",
        name=name or f"snapshot:{session_record.id}",
        session_ids=(session_record.id,),
        observation_ids=session_record.observation_ids or execution_record.observation_ids,
        artifact_ids=session_record.artifact_ids or execution_record.artifact_ids,
        metadata=session_record.metadata + execution_record.metadata,
    )

    dataset_dir = _ensure_dir(_dataset_dir(dataset.id, resolved_root))
    _write_json(dataset_dir / "dataset.json", _serialize_dataset(dataset))

    _print_json({"dataset": _serialize_dataset(dataset), "path": str(dataset_dir)})


@app.command("eval")
def evaluate(
    dataset_ref: str = typer.Argument(..., help="Dataset id, dataset directory, or dataset file."),
    against: str | None = typer.Option(
        None,
        "--against",
        help="Optional dataset id, dataset directory, or execution reference to compare against.",
    ),
    root: Path = typer.Option(
        Path(".glassbox"),
        "--root",
        help="Workspace root used to resolve dataset references.",
        dir_okay=True,
        file_okay=False,
        exists=False,
        resolve_path=False,
    ),
) -> None:
    """Evaluate a dataset against a comparison target and print a summary."""

    resolved_root = _workspace_root(root)
    left = _load_dataset(dataset_ref, resolved_root)
    right = _load_dataset(against, resolved_root) if against is not None else left
    runner = EvaluationRunner()
    result = runner.compare(left, right)
    _print_json(
        {
            "left_dataset": _serialize_dataset(left),
            "right_dataset": _serialize_dataset(right),
            "score": asdict(result.score),
            "diff": asdict(result.diff),
        }
    )


@app.command()
def diff(
    left: str = typer.Argument(..., help="Left dataset or execution reference."),
    right: str = typer.Argument(..., help="Right dataset or execution reference."),
    root: Path = typer.Option(
        Path(".glassbox"),
        "--root",
        help="Workspace root used to resolve dataset references.",
        dir_okay=True,
        file_okay=False,
        exists=False,
        resolve_path=False,
    ),
) -> None:
    """Compare two datasets or executions and print a structured diff."""

    resolved_root = _workspace_root(root)
    left_dataset = _load_dataset(left, resolved_root)
    right_dataset = _load_dataset(right, resolved_root)
    _print_json(asdict(diff_datasets(left_dataset, right_dataset)))


@app.command()
def watch() -> None:
    """[legacy] Launch the Textual UI."""

    GlassboxApp().run()


@app.command()
def demo() -> None:
    """[legacy] Launch the Textual UI in demo mode."""

    GlassboxApp(demo_mode=True).run()


if __name__ == "__main__":
    app()
