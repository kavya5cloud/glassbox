# Dependency Graph

The core architecture is intentionally acyclic.

```mermaid
flowchart TD
  Core[glassbox.core]
  Capture[glassbox.capture]
  Storage[glassbox.storage]
  Semantics[glassbox.semantics]
  Evaluation[glassbox.evaluation]
  SDK[glassbox.sdk]
  TUI[glassbox.tui]
  CLI[glassbox.cli]

  Capture --> Core
  Storage --> Core
  Semantics --> Core
  Evaluation --> Core
  Evaluation --> Storage
  SDK --> Core
  TUI --> SDK
  TUI --> Evaluation
  CLI --> Core
  CLI --> Capture
  CLI --> Storage
  CLI --> Semantics
  CLI --> Evaluation
  CLI --> SDK
  CLI --> TUI
```

Notes:

- Core depends on nothing.
- Capture depends only on Core.
- Storage depends only on Core.
- Semantics depends only on Core.
- Evaluation depends on Core and Storage.
- SDK depends only on Core.
- TUI depends only on SDK and Evaluation.
- CLI depends on the full stack.
