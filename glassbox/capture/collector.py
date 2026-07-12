"""Capture collector.

Public API:
- ObservationCollector

Future extension points:
- sharding
- buffering
- transport retries
"""

from __future__ import annotations

from dataclasses import dataclass, field

from glassbox.core import Observation

from .recorder import Recorder
from .transport import ObservationTransport


@dataclass(slots=True)
class ObservationCollector:
    """Route observations into a recorder and optional transport."""

    transport: ObservationTransport | None = None
    recorder: Recorder = field(init=False)

    def __post_init__(self) -> None:
        self.recorder = Recorder(transport=self.transport)

    def collect(self, observation: Observation) -> None:
        """Record a single observation."""

        self.recorder.record(observation)
