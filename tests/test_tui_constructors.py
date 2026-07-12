from __future__ import annotations

import asyncio
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

from glassbox.tui.app import GlassboxApp
from textual.widgets import Static


def test_glassbox_app_mounts_without_constructor_type_errors() -> None:
    async def run() -> None:
        app = GlassboxApp()
        async with app.run_test() as pilot:
            await pilot.pause()
            widget = app.query_one("#glassbox-core", Static)
            assert widget.id == "glassbox-core"

    asyncio.run(run())


def test_installed_wheel_launches_real_app_without_constructor_type_errors() -> None:
    project_root = Path(__file__).resolve().parents[1]
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir)
        dist_dir = tmp_path / "dist"
        site_dir = tmp_path / "site"
        site_dir.mkdir()

        subprocess.run(
            [
                sys.executable,
                "-m",
                "build",
                "--wheel",
                "--no-isolation",
                "--outdir",
                str(dist_dir),
            ],
            check=True,
            cwd=project_root,
        )

        wheel = next(dist_dir.glob("glassbox-0.2.0-*.whl"))
        subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--no-deps",
                "--target",
                str(site_dir),
                str(wheel),
            ],
            check=True,
            capture_output=True,
        )

        code = textwrap.dedent(
            """
            import sys

            sys.path.insert(0, {site_dir!r})
            from glassbox.tui.app import GlassboxApp


            async def auto_exit(pilot):
                await pilot.pause()
                await pilot.press("q")


            GlassboxApp().run(headless=True, auto_pilot=auto_exit)
            print("app-launched")
            """
        ).format(site_dir=str(site_dir))
        result = subprocess.run(
            [sys.executable, "-c", code],
            check=True,
            capture_output=True,
            text=True,
        )

        assert "app-launched" in result.stdout
        assert "unexpected keyword argument 'id'" not in result.stderr
