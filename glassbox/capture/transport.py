"""Transport interfaces for captured observations.

Public API:
- ObservationTransport

Future extension points:
- OTLP encoders
- batch flushing
- transport backpressure
"""

from __future__ import annotations

from typing import Protocol

from glassbox.core import Observation


class ObservationTransport(Protocol):
    """Send immutable observations to a downstream sink."""

    def send(self, observation: Observation) -> None:
        """Send a single observation."""

    def close(self) -> None:
        """Release any transport resources."""
