"""Profile protocol for converting observations into IR nodes."""

from __future__ import annotations

from typing import Protocol

from .node import Node
from .observation import Observation


class Profile(Protocol):
    """Transform immutable observations into IR nodes."""

    name: str

    def transform(self, observations: tuple[Observation, ...]) -> tuple[Node, ...]:
        """Convert observations into IR nodes."""
