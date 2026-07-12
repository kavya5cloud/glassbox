"""Semantic interpreters for raw observations.

Public API:
- SemanticProfile
- SemanticView
- Interpreter

Future extension points:
- registry-backed discovery
- semantic version negotiation
- framework adapters
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from glassbox.core import Observation


@dataclass(frozen=True, slots=True)
class SemanticProfile:
    """Describe a semantic profile supported by an interpreter."""

    name: str
    version: str
    scope: str


@dataclass(frozen=True, slots=True)
class SemanticView:
    """A read-time interpretation of a raw observation."""

    observation_id: str
    profile_name: str
    profile_version: str
    kind: str
    fields: tuple[tuple[str, str], ...] = ()


class Interpreter(Protocol):
    """Convert an observation into a semantic view."""

    profile: SemanticProfile

    def interpret(self, observation: Observation) -> SemanticView:
        """Interpret one observation."""
