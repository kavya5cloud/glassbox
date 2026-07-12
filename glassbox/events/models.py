"""Legacy event models used by the synthetic event demo helpers."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field


class LLMEvent(BaseModel):
    """A lightweight legacy event shape used by ``glassbox.events.demo``."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    provider: str = Field(default="unknown")
    model: str = Field(default="unknown")
    prompt_tokens: int = Field(default=0)
    completion_tokens: int = Field(default=0)
    latency_ms: int = Field(default=0)
    cost: float = Field(default=0.0)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the event."""
        return self.model_dump(mode="json")
