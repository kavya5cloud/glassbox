"""Deterministic demo engine for scripted trace replay."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Sequence
from uuid import uuid4

from glassbox.tracing import EventBus, Trace


@dataclass(frozen=True)
class DemoStep:
    """Single scripted step emitted by the demo source."""

    provider: str
    model: str
    prompt: str
    response: str
    input_tokens: int
    output_tokens: int
    latency_ms: int
    cost: float
    status: str = "completed"
    notes: str | None = None
    sleep_ms: int = 0


class ScriptedTraceSource:
    """Produce a deterministic sequence of realistic trace steps."""

    def steps(self) -> Sequence[DemoStep]:
        return (
            DemoStep(
                provider="OpenAI",
                model="GPT-5.5",
                prompt="Customer support request: " + "A customer needs help with a failed login and asks for a step-by-step recovery guide.",
                response="I can help you recover your account by resetting the password and verifying the email address.",
                input_tokens=1280,
                output_tokens=340,
                latency_ms=620,
                cost=0.0048,
                status="running",
                notes="request accepted",
                sleep_ms=100,
            ),
            DemoStep(
                provider="Anthropic",
                model="Claude Sonnet 4.5",
                prompt="Customer support request: " + "Summarize the billing dispute and draft a polite response for the customer.",
                response="The customer is disputing a duplicate charge and wants a clear explanation of the billing timeline.",
                input_tokens=1820,
                output_tokens=420,
                latency_ms=880,
                cost=0.0061,
                status="completed",
                notes="billing summary drafted",
                sleep_ms=150,
            ),
            DemoStep(
                provider="Google",
                model="Gemini 2.5 Pro",
                prompt="Customer support request: " + "Analyze the issue logs and suggest the most likely root cause for the authentication outage.",
                response="The outage is most likely caused by a failed token refresh path after a recent certificate rotation.",
                input_tokens=2360,
                output_tokens=510,
                latency_ms=730,
                cost=0.0054,
                status="completed",
                notes="incident guidance produced",
                sleep_ms=120,
            ),
            DemoStep(
                provider="OpenAI",
                model="GPT-5.5",
                prompt="Embedding request: " + "Retrieve semantic embeddings for the support article about password reset troubleshooting.",
                response="Embedding generated for 153 content chunks.",
                input_tokens=6400,
                output_tokens=0,
                latency_ms=420,
                cost=0.0012,
                status="completed",
                notes="vector index refreshed",
                sleep_ms=120,
            ),
            DemoStep(
                provider="Anthropic",
                model="Claude Sonnet 4.5",
                prompt="Tool call: " + "Use the knowledge base search to find the policy article for refund eligibility.",
                response="Tool result: policy article retrieved and summarized.",
                input_tokens=2140,
                output_tokens=280,
                latency_ms=540,
                cost=0.0037,
                status="completed",
                notes="tool execution succeeded",
                sleep_ms=110,
            ),
            DemoStep(
                provider="OpenAI",
                model="GPT-5.5",
                prompt="Slow request: " + "Generate a detailed escalation response for a VIP customer after repeated failed attempts.",
                response="Escalation response prepared with a timeline and recommended next actions.",
                input_tokens=3180,
                output_tokens=640,
                latency_ms=9000,
                cost=0.0142,
                status="completed",
                notes="slow request observed",
                sleep_ms=100,
            ),
            DemoStep(
                provider="OpenAI",
                model="GPT-5.5",
                prompt="Retry request: " + "Try to resolve the payment verification error after a temporary upstream failure.",
                response="The request failed once and succeeded on retry.",
                input_tokens=1450,
                output_tokens=300,
                latency_ms=1180,
                cost=0.0043,
                status="failed",
                notes="transient upstream failure; retried",
                sleep_ms=140,
            ),
            DemoStep(
                provider="Anthropic",
                model="Claude Sonnet 4.5",
                prompt="Support ticket backlog: " + "A very large prompt with repeated ticket history for the last 90 days. " + ("ticket-details " * 6000),
                response="The queue summary and next actions were generated from the long-context backlog.",
                input_tokens=48000,
                output_tokens=960,
                latency_ms=1640,
                cost=0.0214,
                status="completed",
                notes="large context window exercised",
                sleep_ms=180,
            ),
            DemoStep(
                provider="Google",
                model="Gemini 2.5 Pro",
                prompt="Customer support request: " + "Compose a concise handoff summary for the human support team.",
                response="Handoff summary created with the key details and recommended follow-up.",
                input_tokens=2100,
                output_tokens=460,
                latency_ms=670,
                cost=0.0048,
                status="completed",
                notes="handoff complete",
                sleep_ms=130,
            ),
            DemoStep(
                provider="OpenAI",
                model="GPT-5.5",
                prompt="Customer support request: " + "Draft a final resolution message that thanks the customer and confirms the next steps.",
                response="Your issue has been resolved and a follow-up email is on the way.",
                input_tokens=1540,
                output_tokens=360,
                latency_ms=590,
                cost=0.0041,
                status="completed",
                notes="resolution message drafted",
                sleep_ms=110,
            ),
            DemoStep(
                provider="Anthropic",
                model="Claude Sonnet 4.5",
                prompt="Customer support request: " + "Summarize the entire session for the support lead and include the running token and cost totals.",
                response="Session summary complete with cumulative tokens and spend.",
                input_tokens=2240,
                output_tokens=500,
                latency_ms=760,
                cost=0.0056,
                status="completed",
                notes="summary complete",
                sleep_ms=120,
            ),
        )


class DemoEngine:
    """Run the scripted scenario and publish traces into an event bus."""

    def __init__(self, *, bus: EventBus | None = None, source: ScriptedTraceSource | None = None, speed: float = 1.0) -> None:
        self._bus = bus or EventBus()
        self._source = source or ScriptedTraceSource()
        self._speed = speed
        self._started_at: datetime | None = None

    async def run(self, *, collector: list[Trace] | None = None) -> list[Trace]:
        traces: list[Trace] = []
        self._started_at = datetime.now(timezone.utc)

        for step in self._source.steps():
            await asyncio.sleep(step.sleep_ms / 1000.0 * self._speed)

            started_at = datetime.now(timezone.utc)
            start_trace = Trace(
                id=uuid4(),
                provider=step.provider,
                model=step.model,
                input_tokens=step.input_tokens,
                output_tokens=step.output_tokens,
                latency_ms=0,
                cost=round(step.cost / 3.0, 6),
                status="running",
                started_at=started_at,
                ended_at=None,
                prompt=step.prompt,
                response="",
            )
            self._bus.publish(start_trace)
            traces.append(start_trace)
            if collector is not None:
                collector.append(start_trace)

            update_trace = Trace(
                id=uuid4(),
                provider=step.provider,
                model=step.model,
                input_tokens=step.input_tokens,
                output_tokens=step.output_tokens,
                latency_ms=step.latency_ms // 2,
                cost=round(step.cost / 2.0, 6),
                status="updating",
                started_at=started_at,
                ended_at=started_at + timedelta(milliseconds=step.latency_ms // 2),
                prompt=step.prompt,
                response="processing",
            )
            self._bus.publish(update_trace)
            traces.append(update_trace)
            if collector is not None:
                collector.append(update_trace)

            await asyncio.sleep(max(0.01, min(0.08, step.latency_ms / 1000.0 * self._speed / 8.0)))

            completed_trace = Trace(
                id=uuid4(),
                provider=step.provider,
                model=step.model,
                input_tokens=step.input_tokens,
                output_tokens=step.output_tokens,
                latency_ms=step.latency_ms,
                cost=round(step.cost, 6),
                status=step.status,
                started_at=started_at,
                ended_at=started_at + timedelta(milliseconds=step.latency_ms),
                prompt=step.prompt,
                response=step.response,
            )
            self._bus.publish(completed_trace)
            traces.append(completed_trace)
            if collector is not None:
                collector.append(completed_trace)

        return traces
