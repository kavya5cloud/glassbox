"""Pydantic models for reusable trace insights."""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class InsightSeverity(str, Enum):
    """Severity levels for a generated insight."""

    info = "info"
    warning = "warning"
    critical = "critical"


class Insight(BaseModel):
    """A single actionable observation derived from a trace."""

    title: str
    description: str
    severity: InsightSeverity = Field(default=InsightSeverity.info)
    icon: str = Field(default="ℹ")


class SessionStatistics(BaseModel):
    """Optional session-wide context used by insight rules."""

    trace_count: int = Field(default=0)
    total_input_tokens: int = Field(default=0)
    total_output_tokens: int = Field(default=0)
    total_cost: float = Field(default=0.0)
    average_latency_ms: float = Field(default=0.0)
    retry_count: int = Field(default=0)
    error_count: int = Field(default=0)
    largest_prompt_tokens: int = Field(default=0)
    slowest_latency_ms: int = Field(default=0)
    highest_cost_observed: float | None = Field(default=None)
    current_operation: str | None = Field(default=None)
    flags: tuple[str, ...] = Field(default_factory=tuple)
