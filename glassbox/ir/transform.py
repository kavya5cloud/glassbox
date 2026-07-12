"""Helpers for applying IR profiles."""

from __future__ import annotations

from .node import Node
from .observation import Observation
from .profile import Profile


def apply_profile(profile: Profile, observations: tuple[Observation, ...]) -> tuple[Node, ...]:
    """Apply a profile to a fixed set of observations."""

    return profile.transform(observations)
