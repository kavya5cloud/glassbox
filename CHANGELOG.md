# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by Keep a Changelog and this project follows Semantic Versioning where practical.

---

## [0.1.0-alpha] - 2026-07-07

### Added

- Initial public release of Glassbox.
- Terminal-first Textual user interface.
- Core `Trace` model for representing AI interactions.
- Event-driven architecture powered by an Event Bus.
- Live trace feed for monitoring AI requests.
- Trace Inspector for viewing request metadata.
- OpenAI SDK interception foundation.
- Local-first project architecture with zero telemetry philosophy.
- Demo mode foundation for showcasing the interface.
- CLI entrypoint for launching Glassbox.

### Project Structure

- Modular package layout for future providers and plugins.
- Core tracing infrastructure.
- Provider interception layer.
- Textual TUI framework.
- Example applications and test suite.

### Documentation

- Initial README.
- Project roadmap.
- MIT License.
- CHANGELOG.

### Notes

This is the first alpha release of Glassbox and establishes the project's foundation.

Upcoming milestones include:

- SQLite trace recording
- Replay engine
- Anthropic & Gemini support
- Pricing engine
- Prompt diffing
- Plugin SDK
- VS Code integration
