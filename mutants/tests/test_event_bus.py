from __future__ import annotations

from glassbox.tracing.bus import EventBus
from glassbox.tracing.trace import Trace


def test_event_bus_subscribes_once_and_publishes_in_order() -> None:
    bus = EventBus()
    received_one: list[Trace] = []
    received_two: list[Trace] = []

    bus.subscribe(received_one.append)
    bus.subscribe(received_one.append)
    bus.subscribe(received_two.append)

    trace = Trace(provider="OpenAI", model="gpt-4.1")
    bus.publish(trace)

    assert received_one == [trace]
    assert received_two == [trace]
