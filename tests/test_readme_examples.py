from __future__ import annotations

import subprocess
import sys
import textwrap
from pathlib import Path
from types import ModuleType, SimpleNamespace

README = Path(__file__).resolve().parents[1] / "README.md"


def _build_wheel(tmp_path: Path) -> Path:
    dist_dir = tmp_path / "dist"
    subprocess.run(
        [sys.executable, "-m", "build", "--wheel", "--no-isolation", "--outdir", str(dist_dir)],
        check=True,
        cwd=README.parent,
    )
    wheels = sorted(dist_dir.glob("*.whl"))
    assert wheels, "expected a built wheel"
    return wheels[0]


def test_readme_installation_example_builds_and_imports_package(tmp_path) -> None:
    wheel = _build_wheel(tmp_path)
    target_dir = tmp_path / "site"
    target_dir.mkdir()

    subprocess.run(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--no-deps",
            "--target",
            str(target_dir),
            str(wheel),
        ],
        check=True,
        capture_output=True,
    )

    code = textwrap.dedent(
        """
        import sys

        sys.path.insert(0, {target!r})
        import glassbox
        assert glassbox.__version__ == "0.2.0"
        """
    ).format(target=str(target_dir))
    subprocess.run([sys.executable, "-c", code], check=True)


def test_readme_quick_start_example_uses_public_intercept_api(monkeypatch) -> None:
    openai_module = ModuleType("openai")

    class FakeResponses:
        def create(self, *, model, input, **kwargs):
            return SimpleNamespace(
                model=model,
                output=[SimpleNamespace(content=[SimpleNamespace(text="answer")])],
                usage=SimpleNamespace(input_tokens=8, output_tokens=3),
            )

    class FakeOpenAI:
        def __init__(self) -> None:
            self.responses = FakeResponses()

    openai_module.OpenAI = FakeOpenAI
    monkeypatch.setitem(sys.modules, "openai", openai_module)

    namespace: dict[str, object] = {}
    exec(
        textwrap.dedent(
            """
            from glassbox.intercept import intercept
            from openai import OpenAI

            client = intercept(OpenAI())

            client.responses.create(
                model="gpt-4.1",
                input="Explain black holes in one line.",
            )
            """
        ),
        namespace,
    )

    assert isinstance(namespace["client"], object)
    wrapped = namespace["client"]
    assert wrapped.__class__.__name__ == "OpenAIInterceptor"
