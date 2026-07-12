# Data Model

The minimal immutable core should be centered on observations.

## Observation

An observation is an immutable fact captured from runtime behavior:

- timestamp
- session id
- run id
- kind
- payload reference
- identity reference
- parent reference
- relations
- schema version

## Payload Blob

Payloads should be:

- content-addressed
- immutable
- deduplicated
- optionally encrypted

## Identity Fingerprint

Identity should include:

- code version
- prompt version
- model version
- tool version
- environment hash
- dependency hash
- interpreter version

## Relations

Relations connect:

- observation to observation
- session to run
- tool call to parent execution
- derived artifact to source observations

Why this survives:

- raw observations stay stable
- semantics are versioned separately
- derived interpretations can change without rewriting history
- content addressing keeps storage efficient over time

This model is intentionally sparse. Meaning belongs in interpreters, not in the storage schema.
