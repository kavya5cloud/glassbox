"""Legacy event helpers for deterministic demos."""

from .demo import random_event
from .models import LLMEvent

__all__ = ["LLMEvent", "random_event"]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
