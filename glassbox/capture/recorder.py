"""In-memory observation recorder.

Public API:
- Recorder

Future extension points:
- persistence backends
- batch collection
- transport fan-out
"""

from __future__ import annotations

from dataclasses import dataclass, field

from glassbox.core import Observation
from .transport import ObservationTransport


@dataclass(slots=True)
class Recorder:
    """Collect observations and optionally forward them downstream."""

    transport: ObservationTransport | None = None
    _observations: tuple[Observation, ...] = field(init=False, default=())

    def record(self, observation: Observation) -> None:
        """Store an observation locally and forward it if a transport exists."""

        self._observations = (*self._observations, observation)
        if self.transport is not None:
            self.transport.send(observation)

    @property
    def observations(self) -> tuple[Observation, ...]:
        """Return the recorded observations."""

        return self._observations
