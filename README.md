# Glassbox

```
 ██████╗ ██╗      █████╗ ███████╗███████╗██████╗  ██████╗ ██╗  ██╗
██╔════╝ ██║     ██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗╚██╗██╔╝
██║  ███╗██║     ███████║███████╗███████╗██████╔╝██║   ██║ ╚███╔╝
██║   ██║██║     ██╔══██║╚════██║╚════██║██╔══██╗██║   ██║ ██╔██╗
╚██████╔╝███████╗██║  ██║███████║███████║██████╔╝╚██████╔╝██╔╝ ██╗
 ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝

  DevTools for LLM applications
  Inspect every prompt. Replay every run.
  Open source · Local first · Zero telemetry
```    

Wrap your client in one line and watch every LLM call your app makes stream into your terminal — prompts, responses, latency, and token usage, live. No dashboard to deploy, no account, no data leaving your machine.  

[![PyPI](https://img.shields.io/pypi/v/glassbox)](https://pypi.org/project/glassbox)
[![Python](https://img.shields.io/pypi/pyversions/glassbox)](https://pypi.org/project/glassbox)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)

```bash
pip install glassbox
glassbox demo   # try it now
```

> The package is published as **glassbox** on PyPI, and the CLI command and Python package are both named **glassbox**.

---

## Demo

![Glassbox streaming live LLM traces in the terminal](docs/demo.gif)

*A live trace feed on the left, the inspector on the right. Click any call to see the exact prompt that went out and the response that came back.*

---

## Why Glassbox

LLM apps are black boxes. When a response is wrong, a call is slow, or the bill is higher than expected, most people debug by printing `messages` and squinting at raw JSON. You can't see that your "simple" call actually sent 18k tokens, that half of it was duplicated tool schemas, or that the retrieved context never got used.

Glassbox makes every AI call visible — in real time, in your terminal.

**How it's different:** LangSmith and Langfuse are excellent, but they're cloud platforms built for production and teams. Glassbox is for the inner loop — the fast, local, zero-setup iteration you do all day while building. Your traces never leave your machine.

---

## Features

- **Live trace feed** — every request and response, streaming as it happens
- **Trace inspector** — drill into any call: full prompt, response, latency, token usage
- **One-line interception** — wrap the OpenAI SDK and you're done
- **Terminal-first** — a fast Textual UI, no browser, no server to run
- **Demo mode** — see it working in seconds, with no API key
- **Local-first** — SQLite and your filesystem; zero telemetry, zero network calls out

---

## Installation

```bash
pip install glassbox
```

Requires Python 3.9+.

---

## Quick Start

**1. See it work with no setup:**

```bash
glassbox demo
```

This replays synthetic traffic so you can explore the UI before wiring in your own app.

**2. Instrument your app** — wrap your client once:

```python
from glassbox.intercept import intercept
from openai import OpenAI

client = intercept(OpenAI())

client.responses.create(
    model="gpt-4.1",
    input="Explain black holes in one line.",
)
```

**3. Open the terminal UI:**

```bash
glassbox watch
```

Every call your app makes now appears live. Arrow keys to navigate, `Enter` to inspect, `q` to quit.

---

## Architecture

Everything flows through a single interception point and a normalized trace model, so new panels and providers are just new views over the same event stream.


```
   ┌─────────────┐      ┌──────────────┐      ┌────────────┐
   │   Your App  │─────▶│  Interceptor │─────▶│  Provider  │
   └─────────────┘      └──────┬───────┘      └────────────┘
                               │  emits Trace events
                               ▼
                         ┌───────────┐
                         │ Event Bus │
                         └─────┬─────┘
                               │
                               ▼
                         ┌───────────┐
                         │  Terminal │
                         │    UI     │
                         └───────────┘
```

- **Interceptor** — wraps the provider SDK, passes calls straight through, emits a `Trace` for each one.
- **Trace model** — one normalized shape for every AI interaction, whatever the provider.
- **Event bus** — decouples capture from display, so recording, replay, and export can subscribe later without touching the hot path.

---

## Project Structure

```
glassbox/
├── core/        # Trace model, event bus
├── intercept/   # Provider SDK interception
├── ui/          # Textual terminal UI
└── cli.py       # Entry point (demo, ui)
```

---

## Roadmap

<<<<<<< HEAD
=======
**Available now**
>>>>>>> core-rewrite
Today

✅ Process Capture

✅ HTTP Capture

✅ Immutable Observations

✅ Glassbox IR

Next

⬜ Dataset Engine

⬜ Evaluation Engine

⬜ Diff Engine

⬜ Replay

⬜ Deployment Recommendations
---

## Philosophy

**Everything is a trace.** Every AI request should be observable, and that observability should run entirely on your machine. No accounts, no cloud dependency, no telemetry. Glassbox should feel like opening DevTools: it's just there, it's instant, and it shows you what's actually happening.

---

## Contributing

Contributions are welcome. Good places to start:

- Add a provider to `intercept/` (Anthropic and Gemini are open on the roadmap)
- Improve the inspector view in `ui/`
- File an issue with a trace that Glassbox renders poorly

Open an issue to discuss anything larger before sending a PR.

---

## License

Apache 2.0 — see [LICENSE](LICENSE).
