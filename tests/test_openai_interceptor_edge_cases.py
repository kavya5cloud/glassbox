from __future__ import annotations

from types import SimpleNamespace

from glassbox.intercept import intercept
from glassbox.providers.openai import OpenAIInterceptor
from glassbox.tracing import EventBus


class FakeModelLessResponses:
    def create(self, *, input, **kwargs):
        return SimpleNamespace(
            id="resp_456",
            output=[],
            usage=SimpleNamespace(input_tokens=0, output_tokens=0),
        )


class FakeModelLessClient:
    def __init__(self) -> None:
        self.responses = FakeModelLessResponses()


class FakeAzureClient:
    def __init__(self) -> None:
        self.responses = SimpleNamespace()
        self.azure_endpoint = "https://example.openai.azure.com/"


class FakeNoUsageResponses:
    def create(self, *, model, input, **kwargs):
        return SimpleNamespace(
            id="resp_789",
            model=model,
            output=[
                SimpleNamespace(content=[SimpleNamespace(text="Part one")]),
                SimpleNamespace(content=[SimpleNamespace(text="Part two")]),
            ],
        )


class FakeNoUsageClient:
    def __init__(self) -> None:
        self.responses = FakeNoUsageResponses()


class FakeBadModelResponses:
    def create(self, *, model, input, **kwargs):
        return SimpleNamespace(
            id="resp_999",
            model=123,
            output=[],
            usage=SimpleNamespace(input_tokens=0, output_tokens=0),
        )


class FakeBadModelClient:
    def __init__(self) -> None:
        self.responses = FakeBadModelResponses()


def test_openai_interception_handles_empty_prompt_and_unknown_model() -> None:
    client = FakeModelLessClient()
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)

    wrapped = intercept(client, event_bus=bus)
    wrapped.responses.create(input=[])

    assert len(received) == 1
    trace = received[0]
    assert trace.prompt == ""
    assert trace.response == ""
    assert trace.model == "unknown"
    assert trace.input_tokens == 0
    assert trace.output_tokens == 0


def test_openai_supports_rejects_azure_clients() -> None:
    assert OpenAIInterceptor.supports(FakeAzureClient()) is False


def test_openai_interception_handles_responses_without_usage_metadata() -> None:
    client = FakeNoUsageClient()
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)

    wrapped = intercept(client, event_bus=bus)
    wrapped.responses.create(model="gpt-4.1", input="Hello")

    trace = received[0]
    assert trace.response == "Part one\nPart two"
    assert trace.input_tokens == 0
    assert trace.output_tokens == 0


def test_openai_interception_falls_back_when_model_is_not_a_string() -> None:
    client = FakeBadModelClient()
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)

    wrapped = intercept(client, event_bus=bus)
    wrapped.responses.create(model=123, input="Hello")

    trace = received[0]
    assert trace.model == "unknown"
