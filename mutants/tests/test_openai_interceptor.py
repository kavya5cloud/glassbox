from types import SimpleNamespace

from glassbox.intercept import intercept
from glassbox.tracing import EventBus


class FakeOpenAIResponses:
    def create(self, *, model, input, **kwargs):
        return SimpleNamespace(
            id="resp_123",
            model=model,
            output=[SimpleNamespace(content=[SimpleNamespace(text="Hello from Glassbox")])],
            usage=SimpleNamespace(input_tokens=12, output_tokens=7),
        )


class FakeOpenAIClient:
    def __init__(self) -> None:
        self.responses = FakeOpenAIResponses()


def test_intercept_publishes_trace() -> None:
    client = FakeOpenAIClient()
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)

    wrapped = intercept(client, event_bus=bus)
    wrapped.responses.create(model="gpt-4.1", input="Hello")

    assert len(received) == 1
    trace = received[0]
    assert trace.provider == "OpenAI"
    assert trace.model == "gpt-4.1"
    assert trace.prompt == "Hello"
    assert trace.response == "Hello from Glassbox"
    assert trace.input_tokens == 12
    assert trace.output_tokens == 7
    assert trace.status == "completed"


def test_intercept_extracts_text_from_structured_inputs_and_keeps_unicode() -> None:
    client = FakeOpenAIClient()
    bus = EventBus()
    received: list = []
    bus.subscribe(received.append)

    wrapped = intercept(client, event_bus=bus)
    wrapped.responses.create(
        model="gpt-4.1",
        input=[
            {"text": "Olá"},
            " 👋 ",
            {"text": "世界"},
        ],
    )

    trace = received[0]
    assert trace.prompt == "Olá\n 👋 \n世界"
    assert trace.response == "Hello from Glassbox"


def test_intercept_returns_unknown_clients_unchanged() -> None:
    client = object()

    wrapped = intercept(client)

    assert wrapped is client
