from __future__ import annotations

from glassbox.tracing.bus import EventBus
from glassbox.tracing.trace import Trace
from glassbox.tracing.generator import DemoTraceSource


class FakeStopEvent:
    def __init__(self) -> None:
        self.cleared = False
        self.set_called = False
        self._is_set = False

    def clear(self) -> None:
        self.cleared = True
        self._is_set = False

    def set(self) -> None:
        self.set_called = True
        self._is_set = True

    def is_set(self) -> bool:
        return self._is_set


class FakeThread:
    def __init__(self, target, daemon: bool) -> None:
        self.target = target
        self.daemon = daemon
        self.started = False
        self.join_timeout = None
        self._alive = False

    def start(self) -> None:
        self.started = True
        self._alive = True

    def is_alive(self) -> bool:
        return self._alive

    def join(self, timeout: float | None = None) -> None:
        self.join_timeout = timeout
        self._alive = False


def test_demo_trace_source_start_and_stop_manage_background_thread(monkeypatch) -> None:
    bus = EventBus()
    source = DemoTraceSource(bus=bus, interval=0.01)
    fake_stop_event = FakeStopEvent()
    fake_thread = FakeThread(target=source._run, daemon=True)

    monkeypatch.setattr(source, "_stop_event", fake_stop_event)
    monkeypatch.setattr(
        "glassbox.tracing.generator.threading.Thread", lambda target, daemon: fake_thread
    )

    source.start()
    source.start()
    source.stop()

    assert fake_stop_event.cleared is True
    assert fake_stop_event.set_called is True
    assert fake_thread.started is True
    assert fake_thread.join_timeout == 1.0
    assert source._thread is fake_thread


def test_demo_trace_source_generate_trace_uses_sample_payload(monkeypatch) -> None:
    bus = EventBus()
    source = DemoTraceSource(bus=bus, interval=0.01)
    monkeypatch.setattr(source, "_sample_payload", lambda: ("OpenAI", "GPT-5.5", "Hello", "World"))
    monkeypatch.setattr("glassbox.tracing.generator.random.randint", lambda a, b: a)
    monkeypatch.setattr("glassbox.tracing.generator.random.uniform", lambda a, b: a)

    trace = source._generate_trace()

    assert isinstance(trace, Trace)
    assert trace.provider == "OpenAI"
    assert trace.model == "GPT-5.5"
    assert trace.prompt == "Hello"
    assert trace.response == "World"
    assert trace.input_tokens == 80
    assert trace.output_tokens == 40
    assert trace.latency_ms == 180
    assert trace.cost == 0.002
    assert trace.status == "completed"
    assert trace.ended_at is not None
    assert trace.ended_at > trace.started_at


def test_demo_trace_source_samples_known_payloads(monkeypatch) -> None:
    bus = EventBus()
    source = DemoTraceSource(bus=bus, interval=0.01)
    selected = []

    def choose(options):
        selected.append(options)
        return options[1]

    monkeypatch.setattr("glassbox.tracing.generator.random.choice", choose)

    payload = source._sample_payload()

    assert payload == (
        "Anthropic",
        "Claude Sonnet",
        "Draft a concise release summary from the changelog.",
        "The release includes a new event bus and improved storage hooks.",
    )
    assert len(selected) == 1


def test_demo_trace_source_run_publishes_until_stopped(monkeypatch) -> None:
    bus = EventBus()
    source = DemoTraceSource(bus=bus, interval=0.0)
    received: list[Trace] = []

    monkeypatch.setattr(source, "_sample_payload", lambda: ("OpenAI", "GPT-5.5", "Hello", "World"))
    monkeypatch.setattr("glassbox.tracing.generator.random.randint", lambda a, b: a)
    monkeypatch.setattr("glassbox.tracing.generator.random.uniform", lambda a, b: a)
    monkeypatch.setattr("glassbox.tracing.generator.time.sleep", lambda _: None)

    def publish_and_stop(trace: Trace) -> None:
        received.append(trace)
        source._stop_event.set()

    monkeypatch.setattr(bus, "publish", publish_and_stop)

    source._run()

    assert len(received) == 1
    assert received[0].provider == "OpenAI"
