# Capture Layer

Glassbox should capture at multiple boundaries:

- SDK hooks for framework-native integrations
- proxy or gateway capture for language-agnostic traffic
- HTTP middleware for app-level context
- MCP hooks for tool ecosystems
- OpenTelemetry Collector integration for enterprise transport

Capture should always record:

- timestamp
- identity fingerprint
- input/output payload references
- tool calls
- errors
- latency
- token usage when available
- execution relations
- provider/model hints

Capture should never permanently store by default:

- raw secrets
- credentials
- sensitive personal data without policy
- irreversible semantic labels that belong in interpreters

The capture layer should be opinionated about observability and neutral about meaning.
