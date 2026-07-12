from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from glassbox.tracing.builder import TraceBuilder
from glassbox.tracing.bus import EventBus


def test_many_traces_can_be_built_and_published_concurrently() -> None:
    bus = EventBus()
    received = []
    bus.subscribe(received.append)
    builder = TraceBuilder(event_bus=bus)

    def emit(index: int) -> str:
        trace = builder.build(
            provider="OpenAI",
            model=f"gpt-{index % 3}",
            prompt=f"Prompt {index}",
            response_text=f"Response {index}",
            input_tokens=index,
            output_tokens=index + 1,
        )
        builder.publish(trace)
        return str(trace.id)

    with ThreadPoolExecutor(max_workers=16) as pool:
        ids = list(pool.map(emit, range(500)))

    assert len(received) == 500
    assert len(set(ids)) == 500
    assert all(trace.provider == "OpenAI" for trace in received)
