"""Identity fingerprints for execution contexts.

Public API:
- IdentityFingerprint

Future extension points:
- richer normalization for hashes
- signed fingerprints
- environment capsules
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256


@dataclass(frozen=True, slots=True)
class IdentityFingerprint:
    """A stable fingerprint of code, prompt, model, tools, and environment."""

    code_version: str
    prompt_version: str
    model_version: str
    tool_versions: tuple[tuple[str, str], ...] = ()
    environment: str = ""
    dependencies: tuple[tuple[str, str], ...] = ()
    semantic_version: str = "1"

    @classmethod
    def blank(cls) -> "IdentityFingerprint":
        """Return an empty fingerprint for bootstrapping and tests."""

        return cls(
            code_version="",
            prompt_version="",
            model_version="",
        )

    @property
    def digest(self) -> str:
        """Return a content hash for the fingerprint."""

        payload = "|".join(
            [
                self.code_version,
                self.prompt_version,
                self.model_version,
                self._flatten(self.tool_versions),
                self.environment,
                self._flatten(self.dependencies),
                self.semantic_version,
            ]
        )
        return sha256(payload.encode("utf-8")).hexdigest()

    @staticmethod
    def _flatten(pairs: tuple[tuple[str, str], ...]) -> str:
        return ",".join(f"{name}={version}" for name, version in pairs)
