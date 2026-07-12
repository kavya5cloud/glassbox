# RFC-0002: Capture Strategy

Glassbox capture should work across:

- SDKs
- proxies
- HTTP middleware
- MCP
- OpenTelemetry transport

Capture must preserve:

- timing
- tool calls
- model/provider hints
- execution lineage
- identity fingerprints

Capture must avoid permanently storing:

- secrets
- raw credentials
- semantically irreversible labels

Capture is about preserving evidence. Semantics belong in interpreters.
