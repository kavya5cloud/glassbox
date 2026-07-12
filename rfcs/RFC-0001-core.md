# RFC-0001: Core Architecture

This RFC establishes the foundational model:

- sessions as the primary unit of work
- immutable observations as the source of truth
- versioned interpreters for meaning
- identity fingerprints for change attribution
- evaluation as the primary product outcome

Core rules:

- do not bake semantics into storage
- do not treat replay as deterministic
- do not make visualization the product
- do make confidence the product

The long-term system should remain compatible with new frameworks, providers, and execution models without changing the raw data model.
