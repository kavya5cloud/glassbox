"""Trace models for representing LLM request lifecycle data."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTraceǁto_dict__mutmut: MutantDict = {}  # type: ignore


class Trace(BaseModel):
    """Represents a single traced LLM request or response cycle."""

    id: UUID = Field(default_factory=uuid4)
    provider: str = Field(default="unknown")
    model: str = Field(default="unknown")
    input_tokens: int = Field(default=0)
    output_tokens: int = Field(default=0)
    latency_ms: int = Field(default=0)
    cost: float = Field(default=0.0)
    status: str = Field(default="running")
    started_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    ended_at: datetime | None = None
    prompt: str = Field(default="")
    response: str = Field(default="")

    @_mutmut_mutated(mutants_xǁTraceǁto_dict__mutmut)
    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode="json")

    def xǁTraceǁto_dict__mutmut_orig(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode="json")

    def xǁTraceǁto_dict__mutmut_1(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode=None)

    def xǁTraceǁto_dict__mutmut_2(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode="XXjsonXX")

    def xǁTraceǁto_dict__mutmut_3(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode="JSON")

mutants_xǁTraceǁto_dict__mutmut['_mutmut_orig'] = Trace.xǁTraceǁto_dict__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceǁto_dict__mutmut['xǁTraceǁto_dict__mutmut_1'] = Trace.xǁTraceǁto_dict__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTraceǁto_dict__mutmut['xǁTraceǁto_dict__mutmut_2'] = Trace.xǁTraceǁto_dict__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTraceǁto_dict__mutmut['xǁTraceǁto_dict__mutmut_3'] = Trace.xǁTraceǁto_dict__mutmut_3 # type: ignore # mutmut generated
