<div align="center">

# GLASSBOX

```text
 ███  █      ███   ████  ████ ████   ███  █   █
█ ░░░ █░    █ ░░█ █ ░░░░█ ░░░░█░░░█ █ ░░█  █ █ ░
█░ ██░█░░   █████░ ███░░░███░░████░░█░ ░█░  █ ░ ░
█░░ █░█░░   █░░░█░░ ░░█   ░░█ █░░░█ █░░ █░░█ █ ░
 ███ ░█████ █░░░█░████░░████░░████░░ ███ ░█ ░ █
```

### DevTools for LLM Applications.

**Inspect every prompt. Replay every run.**

Open source • Local first • Zero telemetry

---

*Glassbox makes AI applications observable.*

</div>

## Overview

Glassbox is a terminal-first developer tool for inspecting, understanding, and debugging LLM applications.

Instead of treating AI systems as black boxes, Glassbox lets developers observe every request, inspect prompts, replay executions, analyze token usage, and understand exactly what their AI is doing.

Everything runs locally.

No cloud.

No telemetry.

No accounts.

---

## Why?

Modern AI applications are difficult to debug.

Questions like these are surprisingly hard to answer:

- What prompt was actually sent?
- Where did all my tokens go?
- Why did this response change?
- Why is this request expensive?
- Which tool was called?
- What happened during this agent run?

Glassbox aims to answer all of them.

---

## Current Status

🚧 Early development

Current features:

- Terminal UI
- Local-first architecture
- Package scaffolding

Upcoming:

- Live request inspector
- OpenAI support
- Anthropic support
- Replay
- Diff
- Cost analysis
- Security analysis
- Plugin system

---

## Installation

```bash
pip install glassbox
```

or

```bash
pip install -e .
```

---

## Run

```bash
glassbox
```

---

## Roadmap

- [x] Project scaffold
- [x] Terminal UI
- [ ] Event model
- [ ] Live request stream
- [ ] OpenAI interceptor
- [ ] Anthropic interceptor
- [ ] Replay
- [ ] Diff
- [ ] Cost engine
- [ ] Plugin SDK

---

## Philosophy

> Build AI with confidence.

Glassbox exists to make AI systems observable, deterministic, and easier to understand.

---

## License

MIT
