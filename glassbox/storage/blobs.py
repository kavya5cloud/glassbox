"""Content-addressed blob storage.

Public API:
- Blob
- BlobStore
- MemoryBlobStore

Future extension points:
- compression
- encryption
- cloud object stores
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Protocol


@dataclass(frozen=True, slots=True)
class Blob:
    """A content-addressed binary payload."""

    digest: str
    data: bytes
    media_type: str = "application/octet-stream"

    @classmethod
    def from_bytes(cls, data: bytes, *, media_type: str = "application/octet-stream") -> "Blob":
        """Create a blob with a digest derived from the bytes."""

        digest = sha256(data).hexdigest()
        return cls(digest=digest, data=data, media_type=media_type)


class BlobStore(Protocol):
    """Store and retrieve immutable blobs by digest."""

    def put(self, blob: Blob) -> str:
        """Store a blob and return its digest."""

    def get(self, digest: str) -> Blob | None:
        """Return a blob by digest if it exists."""


class MemoryBlobStore:
    """An in-memory blob store for local development and tests."""

    def __init__(self) -> None:
        self._blobs: dict[str, Blob] = {}

    def put(self, blob: Blob) -> str:
        self._blobs[blob.digest] = blob
        return blob.digest

    def get(self, digest: str) -> Blob | None:
        return self._blobs.get(digest)
