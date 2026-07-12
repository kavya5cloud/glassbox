"""Semantic interpretation layer for Glassbox.

Public API:
- SemanticProfile
- SemanticView
- Interpreter

Future extension points:
- framework-specific interpreters
- profile registries
- version negotiation
"""

from .interpreter import Interpreter, SemanticProfile, SemanticView

__all__ = ["Interpreter", "SemanticProfile", "SemanticView"]
