"""Mutation testing configuration for Glassbox."""

source_paths = ["glassbox"]

pytest_add_cli_args_test_selection = ["tests"]

do_not_mutate = [
    "glassbox/demo/*",
    "glassbox/insights/*",
    "glassbox/tui/*",
    "glassbox/storage/*",
    "glassbox/core/*",
    "glassbox/providers/registry.py",
    "glassbox/intercept/openai.py",
    "glassbox/providers/_passthrough.py",
    "glassbox/providers/__init__.py",
    "glassbox/intercept/base.py",
    "glassbox/intercept/anthropic.py",
    "glassbox/providers/base.py",
]
