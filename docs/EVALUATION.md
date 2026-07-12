# Evaluation Engine

The evaluation engine is the heart of the product.

It should compare:

- prompt A vs prompt B
- GPT-5 vs Claude
- tool v1 vs tool v2
- agent v1 vs agent v2

Evaluation types:

- deterministic checks
- rubric scoring
- semantic scoring
- model-as-judge scoring
- human review
- policy checks
- regression classification

Outputs:

- scores
- confidence intervals where possible
- failure modes
- regression labels
- deployment recommendation

The engine should answer:

- did quality improve?
- did cost change?
- did latency change?
- did tool behavior change?
- did the session diverge?
- should this go out?

Replay is useful only when it informs evaluation. The product is not replay itself; the product is confidence.
