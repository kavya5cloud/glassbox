"""Mock trace generation for local development and testing."""

from __future__ import annotations

import random
import threading
import time
from datetime import datetime, timedelta, timezone
from typing import Callable

from .bus import EventBus
from .trace import Trace


class DemoTraceSource:
    """Periodically generates realistic fake traces and publishes them."""

    def __init__(self, bus: EventBus, interval: float = 2.0) -> None:
        self._bus = bus
        self._interval = interval
        self._stop_event = threading.Event()
        self._thread: threading.Thread | None = None

    def start(self) -> None:
        """Start the background trace generation loop."""
        if self._thread and self._thread.is_alive():
            return

        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        """Stop the background trace generation loop."""
        self._stop_event.set()
        if self._thread is not None:
            self._thread.join(timeout=1.0)

    def _run(self) -> None:
        while not self._stop_event.is_set():
            trace = self._generate_trace()
            self._bus.publish(trace)
            time.sleep(self._interval)

    def _generate_trace(self) -> Trace:
        provider, model, prompt, response = self._sample_payload()
        started_at = datetime.now(timezone.utc)
        latency_ms = random.randint(180, 1800)
        input_tokens = random.randint(80, 260)
        output_tokens = random.randint(40, 180)
        cost = round(random.uniform(0.002, 0.08), 6)
        ended_at = started_at + timedelta(milliseconds=latency_ms)

        return Trace(
            provider=provider,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            latency_ms=latency_ms,
            cost=cost,
            status="completed",
            started_at=started_at,
            ended_at=ended_at,
            prompt=prompt,
            response=response,
        )

    def _sample_payload(self) -> tuple[str, str, str, str]:
        provider_model_pairs: list[tuple[str, str, str, str]] = [
            (
                "OpenAI",
                "GPT-5.5",
                "Summarize the latest pull request notes for the team.",
                "The PR adds a cleaner trace event pipeline and improves error handling.",
            ),
            (
                "Anthropic",
                "Claude Sonnet",
                "Draft a concise release summary from the changelog.",
                "The release includes a new event bus and improved storage hooks.",
            ),
            (
                "Google",
                "Gemini 2.5",
                "Explain the root cause of the packaging metadata issue.",
                "The issue was caused by incompatible license metadata emitted by the build backend.",
            ),
        ]
        return random.choice(provider_model_pairs)
