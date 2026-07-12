"""Capture layer for Glassbox.

Public API:
- ObservationTransport
- Recorder
- ObservationCollector

Future extension points:
- SDK hooks
- transport adapters
- collector multiplexing
"""

from .collector import ObservationCollector
from .recorder import Recorder
from .transport import ObservationTransport

__all__ = ["ObservationCollector", "ObservationTransport", "Recorder"]
