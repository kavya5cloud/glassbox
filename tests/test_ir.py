from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from glassbox.ir import Node, Observation, apply_profile
from glassbox.ir.profiles import HTTPProfile


def _run(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, capture_output=True, text=True, check=True)


def test_capture_observations_can_be_transformed_into_ir(tmp_path) -> None:
    script = tmp_path / "agent.py"
    script.write_text("print('ok')\n", encoding="utf-8")
    result = _run(["glassbox", "capture", sys.executable, "agent.py"], cwd=tmp_path)
    match = re.search(r"Session created:\n(?P<session_id>session-[^\n]+)", result.stdout)
    assert match is not None
    session_dir = tmp_path / ".glassbox" / "sessions" / match.group("session_id")
    raw_observations = [
        json.loads(line)
        for line in (session_dir / "observations.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    observations = tuple(Observation.from_mapping(payload) for payload in raw_observations)
    nodes = apply_profile(HTTPProfile(), observations)

    assert len(nodes) == len(observations)
    assert [node.kind for node in nodes] == ["process.started", "process.finished"]
    assert nodes[0].attributes[0] == ("command", json.dumps([sys.executable, "agent.py"]))


def test_capture_does_not_import_ir_directly() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "import sys, glassbox.capture.http; print('glassbox.ir' in sys.modules)",
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert result.stdout.strip() == "False"


def test_profiles_are_replaceable_plugins() -> None:
    class CustomProfile:
        name = "custom"

        def transform(self, observations: tuple[Observation, ...]):
            return tuple(
                Node(id=observation.id, kind="custom.node", occurred_at=observation.occurred_at)
                for observation in observations
            )

    observation = Observation.from_mapping(
        {
            "id": "observation-1",
            "kind": "custom",
            "occurred_at": "2026-07-12T11:31:14.961821+00:00",
            "value": "hello",
        }
    )
    nodes = apply_profile(CustomProfile(), (observation,))

    assert len(nodes) == 1
    assert nodes[0].kind == "custom.node"
