import random
from uuid import uuid4

from .models import LLMEvent

MODELS = [
    ("OpenAI", "GPT-5.5"),
    ("Anthropic", "Claude Sonnet"),
    ("Google", "Gemini 2.5"),
]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_random_event__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_random_event__mutmut)
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

def x_random_event__mutmut_orig() -> LLMEvent:
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

def x_random_event__mutmut_1() -> LLMEvent:
    provider, model = None

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_2() -> LLMEvent:
    provider, model = random.choice(None)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_3() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=None,
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_4() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=None,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_5() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=None,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_6() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=None,
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_7() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=None,
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_8() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=None,
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_9() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=None,
    )

def x_random_event__mutmut_10() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_11() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_12() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_13() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_14() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_15() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_16() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        )

def x_random_event__mutmut_17() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(None),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_18() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(None, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_19() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, None),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_20() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_21() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, ),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_22() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(501, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_23() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5001),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_24() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(None, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_25() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, None),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_26() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_27() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, ),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_28() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(51, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_29() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 801),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_30() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(None, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_31() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, None),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_32() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_33() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, ),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_34() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(401, 3000),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_35() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3001),
        cost=round(random.uniform(0.003, 0.045), 3),
    )

def x_random_event__mutmut_36() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(None, 3),
    )

def x_random_event__mutmut_37() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), None),
    )

def x_random_event__mutmut_38() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(3),
    )

def x_random_event__mutmut_39() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), ),
    )

def x_random_event__mutmut_40() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(None, 0.045), 3),
    )

def x_random_event__mutmut_41() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, None), 3),
    )

def x_random_event__mutmut_42() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.045), 3),
    )

def x_random_event__mutmut_43() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, ), 3),
    )

def x_random_event__mutmut_44() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(1.003, 0.045), 3),
    )

def x_random_event__mutmut_45() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 1.045), 3),
    )

def x_random_event__mutmut_46() -> LLMEvent:
    provider, model = random.choice(MODELS)

    return LLMEvent(
        id=str(uuid4()),
        provider=provider,
        model=model,
        prompt_tokens=random.randint(500, 5000),
        completion_tokens=random.randint(50, 800),
        latency_ms=random.randint(400, 3000),
        cost=round(random.uniform(0.003, 0.045), 4),
    )

mutants_x_random_event__mutmut['_mutmut_orig'] = x_random_event__mutmut_orig # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_1'] = x_random_event__mutmut_1 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_2'] = x_random_event__mutmut_2 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_3'] = x_random_event__mutmut_3 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_4'] = x_random_event__mutmut_4 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_5'] = x_random_event__mutmut_5 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_6'] = x_random_event__mutmut_6 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_7'] = x_random_event__mutmut_7 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_8'] = x_random_event__mutmut_8 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_9'] = x_random_event__mutmut_9 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_10'] = x_random_event__mutmut_10 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_11'] = x_random_event__mutmut_11 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_12'] = x_random_event__mutmut_12 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_13'] = x_random_event__mutmut_13 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_14'] = x_random_event__mutmut_14 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_15'] = x_random_event__mutmut_15 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_16'] = x_random_event__mutmut_16 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_17'] = x_random_event__mutmut_17 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_18'] = x_random_event__mutmut_18 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_19'] = x_random_event__mutmut_19 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_20'] = x_random_event__mutmut_20 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_21'] = x_random_event__mutmut_21 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_22'] = x_random_event__mutmut_22 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_23'] = x_random_event__mutmut_23 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_24'] = x_random_event__mutmut_24 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_25'] = x_random_event__mutmut_25 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_26'] = x_random_event__mutmut_26 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_27'] = x_random_event__mutmut_27 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_28'] = x_random_event__mutmut_28 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_29'] = x_random_event__mutmut_29 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_30'] = x_random_event__mutmut_30 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_31'] = x_random_event__mutmut_31 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_32'] = x_random_event__mutmut_32 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_33'] = x_random_event__mutmut_33 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_34'] = x_random_event__mutmut_34 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_35'] = x_random_event__mutmut_35 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_36'] = x_random_event__mutmut_36 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_37'] = x_random_event__mutmut_37 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_38'] = x_random_event__mutmut_38 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_39'] = x_random_event__mutmut_39 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_40'] = x_random_event__mutmut_40 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_41'] = x_random_event__mutmut_41 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_42'] = x_random_event__mutmut_42 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_43'] = x_random_event__mutmut_43 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_44'] = x_random_event__mutmut_44 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_45'] = x_random_event__mutmut_45 # type: ignore # mutmut generated
mutants_x_random_event__mutmut['x_random_event__mutmut_46'] = x_random_event__mutmut_46 # type: ignore # mutmut generated
