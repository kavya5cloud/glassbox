"""Tracing primitives for Glassbox."""

from .bus import EventBus
from .generator import DemoTraceSource
from .trace import Trace

__all__ = ["EventBus", "Trace", "DemoTraceSource"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
