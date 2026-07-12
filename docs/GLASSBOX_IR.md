# Glassbox IR

Glassbox IR is the smallest stable representation shared by capture, profiles, and future framework adapters.

## Why it exists

Raw observations are useful for recording what happened, but they are not a stable integration boundary. Different runtimes produce different shapes, and those shapes tend to drift as capture grows. IR gives Glassbox one neutral language for execution, nodes, edges, identities, and artifacts.

## Why it is provider-neutral

IR does not know about OpenAI, Anthropic, Gemini, HTTP clients, or any other provider-specific surface. It only describes durable facts. That makes it possible to add or replace providers without changing the internal graph model.

## Why evaluation depends on IR instead of observations

Observations are capture-time records. They are intentionally close to the source process and can include framework- or transport-specific details. Evaluation should work on IR because IR is the normalized, comparable layer. That lets evaluation stay consistent even when capture formats change.

## Current path

Observation
-> Profile
-> IR

The HTTP profile is the first proof point for this pipeline.
