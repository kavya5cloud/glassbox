import asyncio

from glassbox.demo import DemoEngine, ScriptedTraceSource
from glassbox.tracing import EventBus


def test_demo_engine_emits_deterministic_trace_sequence() -> None:
    bus = EventBus()
    traces: list = []
    engine = DemoEngine(bus=bus, source=ScriptedTraceSource(), speed=0.0)

    asyncio.run(engine.run(collector=traces))

    assert len(traces) >= 12

    first = traces[0]
    assert first.provider == "OpenAI"
    assert first.status == "running"
    assert first.prompt.startswith("Customer support request")

    assert any(trace.status == "updating" for trace in traces)

    completed = [trace for trace in traces if trace.status == "completed"]
    assert any(trace.provider == "Anthropic" and trace.model == "Claude Sonnet 4.5" for trace in completed)
    assert any(trace.provider == "Google" and trace.model == "Gemini 2.5 Pro" for trace in completed)

    large_prompt = next(trace for trace in traces if trace.input_tokens > 40000)
    assert large_prompt.prompt.startswith("Support ticket backlog")
    assert large_prompt.input_tokens > 40000

    failed_retry = [trace for trace in traces if trace.status == "failed"]
    assert len(failed_retry) >= 1
    assert any(trace.provider == "OpenAI" and trace.model == "GPT-5.5" for trace in failed_retry)
