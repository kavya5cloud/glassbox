from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path


def test_built_wheel_uses_project_name_and_includes_tui_stylesheet(tmp_path) -> None:
    dist_dir = tmp_path / "dist"
    subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--no-isolation", "--outdir", str(dist_dir)],
        check=True,
        cwd=Path(__file__).resolve().parents[1],
    )

    wheels = sorted(dist_dir.glob("*.whl"))
    assert len(wheels) == 1
    wheel = wheels[0]

    assert wheel.name.startswith("glassbox-0.2.0")

    with zipfile.ZipFile(wheel) as archive:
        names = set(archive.namelist())

    assert "glassbox/tui/glassbox.tcss" in names
