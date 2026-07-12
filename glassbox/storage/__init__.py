"""Storage primitives for Glassbox.

Public API:
- Blob
- BlobStore
- MetadataStore
- Dataset
- DatasetStore

Future extension points:
- hot/cold tiering
- columnar analytics
- retention policies
"""

from .blobs import Blob, BlobStore, MemoryBlobStore
from .datasets import Dataset, DatasetStore, MemoryDatasetStore
from .metadata import MetadataEntry, MetadataStore, MemoryMetadataStore

__all__ = [
    "Blob",
    "BlobStore",
    "Dataset",
    "DatasetStore",
    "MemoryBlobStore",
    "MemoryDatasetStore",
    "MetadataEntry",
    "MetadataStore",
    "MemoryMetadataStore",
]
