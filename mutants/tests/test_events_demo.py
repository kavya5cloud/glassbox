from __future__ import annotations

from glassbox.events.demo import random_event
from glassbox.events.models import LLMEvent


def test_random_event_generates_legacy_event_payload(monkeypatch) -> None:
    monkeypatch.setattr("glassbox.events.demo.random.choice", lambda seq: seq[0])
    monkeypatch.setattr("glassbox.events.demo.random.randint", lambda a, b: a)
    monkeypatch.setattr("glassbox.events.demo.random.uniform", lambda a, b: a)

    event = random_event()

    assert isinstance(event, LLMEvent)
    assert event.provider == "OpenAI"
    assert event.model == "GPT-5.5"
    assert event.prompt_tokens == 500
    assert event.completion_tokens == 50
    assert event.latency_ms == 400
    assert event.cost == 0.003
    assert len(event.id) > 0

    payload = event.to_dict()
    assert payload["provider"] == "OpenAI"
    assert payload["prompt_tokens"] == 500
