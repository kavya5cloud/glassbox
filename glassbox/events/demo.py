import random
from uuid import uuid4

from .models import LLMEvent

MODELS = [
    ("OpenAI", "GPT-5.5"),
    ("Anthropic", "Claude Sonnet"),
    ("Google", "Gemini 2.5"),
]

def random_event() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )
