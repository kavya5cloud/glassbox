# High-Level Architecture

Glassbox should be organized around the following layers:

```mermaid
flowchart LR
  subgraph Capture
    SDK[SDK Hooks]
    Proxy[Proxy / Gateway]
    HTTP[HTTP Middleware]
    MCP[MCP Hooks]
    OTel[OpenTelemetry Collector]
  end

  subgraph Transport
    OTLP[OTLP / Event Stream]
  end

  subgraph Storage
    Hot[Hot Store]
    Cold[Cold Blob Store]
    Columnar[Columnar Analytics]
    Index[Index / Catalog]
  end

  subgraph Semantic
    IDL[Identity Engine]
    INT[Interpreter Registry]
    SEM[Semantic Views]
  end

  subgraph Engines
    Eval[Evaluation Engine]
    Data[Dataset Engine]
    Exec[Execution Engine]
    Diff[Diff Engine]
  end

  subgraph Extensibility
    Plug[Plugin Runtime]
  end

  subgraph Surfaces
    CLI[CLI]
    TUI[TUI]
    Desk[Desktop]
    IDE[IDE Integrations]
    Browser[Browser Integrations]
    CI[CI Integrations]
    Cloud[Cloud]
  end

  SDK --> OTLP
  Proxy --> OTLP
  HTTP --> OTLP
  MCP --> OTLP
  OTel --> OTLP
  OTLP --> Hot
  OTLP --> Cold
  Hot --> Index
  Cold --> Columnar
  Index --> INT
  Index --> IDL
  IDL --> SEM
  INT --> SEM
  SEM --> Eval
  SEM --> Data
  SEM --> Diff
  Data --> Eval
  Eval --> Exec
  Exec --> Diff
  Plug --> SDK
  Plug --> IDE
  Plug --> Browser
  Plug --> CI
  Plug --> Cloud
```

Core idea:

- capture gathers facts
- transport moves facts reliably
- storage preserves raw evidence and derived artifacts separately
- identity explains what changed
- semantics are applied at read time
- evaluation decides whether a change is safe
- execution supports re-run and simulation
- plugins connect external ecosystems without hard-coding them into the core

The product should optimize for confidence, not just visibility.
