"""Trace models for representing LLM request lifecycle data."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


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

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable representation of the trace."""
        return self.model_dump(mode="json")
