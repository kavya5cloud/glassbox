"""Glassbox intermediate representation.

Public API:
- Identity
- Execution
- Node
- Edge
- Artifact
- Observation
- Profile
- apply_profile

Future extension points:
- provider adapters
- framework adapters
- evaluation graphing
"""

from .artifact import Artifact
from .edge import Edge
from .execution import Execution
from .identity import Identity
from .node import Node
from .observation import Observation
from .profile import Profile
from .transform import apply_profile

__all__ = [
    "Artifact",
    "Edge",
    "Execution",
    "Identity",
    "Node",
    "Observation",
    "Profile",
    "apply_profile",
]
