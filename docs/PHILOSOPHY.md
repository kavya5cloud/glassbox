# Philosophy

Core principles:

- Build on OpenTelemetry, do not replace it.
- OTLP is transport, not the product.
- Store immutable raw observations.
- Never permanently bake semantics into storage.
- Interpret observations at read time using versioned semantic interpreters.
- Make the session the primary unit of understanding.
- Treat evaluation as the center of gravity.
- Treat replay as a tool for comparison, not as a promise of determinism.
- Prefer local-first workflows.
- Keep the architecture framework-neutral, provider-neutral, and language-neutral.

Non-goals:

- Not a provider SDK wrapper.
- Not a single-vendor observability dashboard.
- Not a logging system.
- Not a deterministic replay engine.
- Not a storage format that hard-codes one framework forever.

Tradeoffs:

- We accept more architectural layering in exchange for long-term semantic flexibility.
- We accept versioned interpreters instead of irreversible storage semantics.
- We accept that re-execution is probabilistic and must report confidence, not certainty.

What Glassbox should never become:

- A pretty dashboard with no decision value.
- A system that requires production traffic to be useful.
- A product that loses meaning as frameworks evolve.
- A monolith that cannot host plugins or new interpreters.
