# Storage

Storage should be split by purpose:

- hot store for recent sessions, indexes, and fast UI queries
- cold blob store for immutable payloads and artifacts
- columnar analytics store for large-scale evaluation and aggregation
- search or catalog store for retrieval and semantic lookup

Rules:

- immutable observations are append-only
- derived artifacts are reproducible, not canonical
- deduplication should happen on content-addressed blobs
- retention should be policy-driven
- compression should be transparent

This split lets Glassbox stay fast for local work and scalable for fleet analysis.
