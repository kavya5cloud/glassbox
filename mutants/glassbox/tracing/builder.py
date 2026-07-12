"""Builds Trace objects from provider-specific response data."""

from __future__ import annotations

from datetime import datetime, timezone

from glassbox.tracing import Trace
from glassbox.tracing.bus import EventBus, default_bus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁTraceBuilderǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTraceBuilderǁbuild__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTraceBuilderǁpublish__mutmut: MutantDict = {}  # type: ignore


class TraceBuilder:
    """Convert provider-specific data into a Trace and publish it."""

    @_mutmut_mutated(mutants_xǁTraceBuilderǁ__init____mutmut)
    def __init__(self, event_bus: EventBus | None = None) -> None:
        self._event_bus = event_bus or default_bus

    def xǁTraceBuilderǁ__init____mutmut_orig(self, event_bus: EventBus | None = None) -> None:
        self._event_bus = event_bus or default_bus

    def xǁTraceBuilderǁ__init____mutmut_1(self, event_bus: EventBus | None = None) -> None:
        self._event_bus = None

    def xǁTraceBuilderǁ__init____mutmut_2(self, event_bus: EventBus | None = None) -> None:
        self._event_bus = event_bus and default_bus

    @_mutmut_mutated(mutants_xǁTraceBuilderǁbuild__mutmut)
    def build(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_orig(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_1(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "XXcompletedXX",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_2(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "COMPLETED",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_3(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = None
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_4(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at and datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_5(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(None)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_6(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = None
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_7(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at and started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_8(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is not None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_9(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = None
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_10(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int(None)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_11(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() / 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_12(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended + started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_13(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1001)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_14(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is not None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_15(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = None

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_16(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 1.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_17(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=None,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_18(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=None,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_19(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=None,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_20(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=None,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_21(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=None,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_22(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=None,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_23(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=None,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_24(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=None,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_25(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=None,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_26(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=None,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_27(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=None,
        )

    def xǁTraceBuilderǁbuild__mutmut_28(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_29(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_30(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_31(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_32(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_33(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_34(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_35(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            ended_at=ended,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_36(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            prompt=prompt,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_37(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            response=response_text,
        )

    def xǁTraceBuilderǁbuild__mutmut_38(
        self,
        *,
        provider: str,
        model: str,
        prompt: str,
        response_text: str,
        input_tokens: int,
        output_tokens: int,
        started_at: datetime | None = None,
        ended_at: datetime | None = None,
        status: str = "completed",
        latency_ms: int | None = None,
        cost: float | None = None,
    ) -> Trace:
        """Construct a Trace from normalized provider data."""
        started = started_at or datetime.now(timezone.utc)
        ended = ended_at or started
        if latency_ms is None:
            latency_ms = int((ended - started).total_seconds() * 1000)
        if cost is None:
            cost = 0.0

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status=status,
            started_at=started,
            ended_at=ended,
            prompt=prompt,
            )

    @_mutmut_mutated(mutants_xǁTraceBuilderǁpublish__mutmut)
    def publish(self, trace: Trace) -> None:
        """Publish a built trace through the configured event bus."""
        self._event_bus.publish(trace)

    def xǁTraceBuilderǁpublish__mutmut_orig(self, trace: Trace) -> None:
        """Publish a built trace through the configured event bus."""
        self._event_bus.publish(trace)

    def xǁTraceBuilderǁpublish__mutmut_1(self, trace: Trace) -> None:
        """Publish a built trace through the configured event bus."""
        self._event_bus.publish(None)

mutants_xǁTraceBuilderǁ__init____mutmut['_mutmut_orig'] = TraceBuilder.xǁTraceBuilderǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁ__init____mutmut['xǁTraceBuilderǁ__init____mutmut_1'] = TraceBuilder.xǁTraceBuilderǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁ__init____mutmut['xǁTraceBuilderǁ__init____mutmut_2'] = TraceBuilder.xǁTraceBuilderǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁTraceBuilderǁbuild__mutmut['_mutmut_orig'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_1'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_2'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_3'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_3 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_4'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_4 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_5'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_5 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_6'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_6 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_7'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_7 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_8'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_8 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_9'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_9 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_10'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_10 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_11'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_11 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_12'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_12 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_13'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_13 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_14'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_14 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_15'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_15 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_16'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_16 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_17'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_17 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_18'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_18 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_19'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_19 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_20'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_20 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_21'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_21 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_22'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_22 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_23'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_23 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_24'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_24 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_25'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_25 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_26'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_26 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_27'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_27 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_28'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_28 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_29'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_29 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_30'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_30 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_31'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_31 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_32'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_32 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_33'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_33 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_34'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_34 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_35'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_35 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_36'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_36 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_37'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_37 # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁbuild__mutmut['xǁTraceBuilderǁbuild__mutmut_38'] = TraceBuilder.xǁTraceBuilderǁbuild__mutmut_38 # type: ignore # mutmut generated

mutants_xǁTraceBuilderǁpublish__mutmut['_mutmut_orig'] = TraceBuilder.xǁTraceBuilderǁpublish__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTraceBuilderǁpublish__mutmut['xǁTraceBuilderǁpublish__mutmut_1'] = TraceBuilder.xǁTraceBuilderǁpublish__mutmut_1 # type: ignore # mutmut generated
