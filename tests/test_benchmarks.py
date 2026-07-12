from __future__ import annotations

from types import SimpleNamespace

import pytest

pytest.importorskip("pytest_benchmark")

from glassbox.intercept import intercept
from glassbox.tracing import EventBus, Trace
from glassbox.tracing.builder import TraceBuilder
from glassbox.tracing.generator import DemoTraceSource


class FakeResponses:
    def create(self, *, model, input, **kwargs):
        return SimpleNamespace(
            model=model,
            output=[SimpleNamespace(content=[SimpleNamespace(text="ok")])],
            usage=SimpleNamespace(input_tokens=4, output_tokens=2),
        )


class FakeOpenAIClient:
    def __init__(self) -> None:
        self.responses = FakeResponses()


def test_benchmark_provider_interception(benchmark) -> None:
    client = FakeOpenAIClient()
    wrapped = intercept(client)

    def run() -> None:
        wrapped.responses.create(model="gpt-4.1", input="hello")

    benchmark(run)


def test_benchmark_trace_creation(benchmark) -> None:
    builder = TraceBuilder()

    def run() -> Trace:
        return builder.build(
            provider="OpenAI",
            model="gpt-4.1",
            prompt="hello",
            response_text="world",
            input_tokens=4,
            output_tokens=2,
        )

    trace = benchmark(run)
    assert trace.provider == "OpenAI"


def test_benchmark_event_publishing(benchmark) -> None:
    bus = EventBus()
    bus.subscribe(lambda trace: None)
    trace = Trace(provider="OpenAI", model="gpt-4.1")

    def run() -> None:
        bus.publish(trace)

    benchmark(run)


def test_benchmark_serialization(benchmark) -> None:
    trace = Trace(provider="OpenAI", model="gpt-4.1", prompt="hello", response="world")

    payload = benchmark(trace.to_dict)
    assert payload["provider"] == "OpenAI"


def test_benchmark_generator_throughput(monkeypatch, benchmark) -> None:
    source = DemoTraceSource(bus=EventBus(), interval=0.0)
    monkeypatch.setattr(source, "_sample_payload", lambda: ("OpenAI", "GPT-5.5", "hello", "world"))
    monkeypatch.setattr("glassbox.tracing.generator.random.randint", lambda a, b: a)
    monkeypatch.setattr("glassbox.tracing.generator.random.uniform", lambda a, b: a)

    trace = benchmark(source._generate_trace)
    assert trace.model == "GPT-5.5"
