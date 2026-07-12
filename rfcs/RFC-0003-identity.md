# RFC-0003: Identity Strategy

Identity is how Glassbox explains change.

Every execution should be fingerprinted with:

- code version
- prompt version
- model version
- tool version
- environment hash
- dependency hash
- interpreter version

Identity is required so evaluation and diffing can answer not just what happened, but what changed.

Without identity, sessions become hard to compare, regressions become hard to reproduce, and confidence decays.
