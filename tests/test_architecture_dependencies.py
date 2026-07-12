from __future__ import annotations

import importlib


DEPENDENCIES: dict[str, tuple[str, ...]] = {
    "glassbox.core": (),
    "glassbox.capture": ("glassbox.core",),
    "glassbox.storage": ("glassbox.core",),
    "glassbox.semantics": ("glassbox.core",),
    "glassbox.evaluation": ("glassbox.core", "glassbox.storage"),
    "glassbox.sdk": ("glassbox.core",),
    "glassbox.tui": ("glassbox.sdk", "glassbox.evaluation"),
    "glassbox.cli": (
        "glassbox.core",
        "glassbox.capture",
        "glassbox.storage",
        "glassbox.semantics",
        "glassbox.evaluation",
        "glassbox.sdk",
        "glassbox.tui",
    ),
}


def test_core_architecture_modules_import() -> None:
    for module_name in DEPENDENCIES:
        module = importlib.import_module(module_name)
        assert module is not None


def test_core_architecture_dependency_graph_is_acyclic() -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(module_name: str) -> None:
        if module_name in visited:
            return
        if module_name in visiting:
            raise AssertionError(f"cycle detected at {module_name}")
        visiting.add(module_name)
        for dependency in DEPENDENCIES[module_name]:
            visit(dependency)
        visiting.remove(module_name)
        visited.add(module_name)

    for module_name in DEPENDENCIES:
        visit(module_name)
