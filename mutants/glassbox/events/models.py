"""Legacy event models used by the synthetic event demo helpers."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁLLMEventǁto_dict__mutmut: MutantDict = {}  # type: ignore


class LLMEvent(BaseModel):
    """A lightweight legacy event shape used by ``glassbox.events.demo``."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    provider: str = Field(default="unknown")
    model: str = Field(default="unknown")
    prompt_tokens: int = Field(default=0)
    completion_tokens: int = Field(default=0)
    latency_ms: int = Field(default=0)
    cost: float = Field(default=0.0)

    @_mutmut_mutated(mutants_xǁLLMEventǁto_dict__mutmut)
    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode="json")

    def xǁLLMEventǁto_dict__mutmut_orig(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode="json")

    def xǁLLMEventǁto_dict__mutmut_1(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode=None)

    def xǁLLMEventǁto_dict__mutmut_2(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode="XXjsonXX")

    def xǁLLMEventǁto_dict__mutmut_3(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode="JSON")

mutants_xǁLLMEventǁto_dict__mutmut['_mutmut_orig'] = LLMEvent.xǁLLMEventǁto_dict__mutmut_orig # type: ignore # mutmut generated
mutants_xǁLLMEventǁto_dict__mutmut['xǁLLMEventǁto_dict__mutmut_1'] = LLMEvent.xǁLLMEventǁto_dict__mutmut_1 # type: ignore # mutmut generated
mutants_xǁLLMEventǁto_dict__mutmut['xǁLLMEventǁto_dict__mutmut_2'] = LLMEvent.xǁLLMEventǁto_dict__mutmut_2 # type: ignore # mutmut generated
mutants_xǁLLMEventǁto_dict__mutmut['xǁLLMEventǁto_dict__mutmut_3'] = LLMEvent.xǁLLMEventǁto_dict__mutmut_3 # type: ignore # mutmut generated
