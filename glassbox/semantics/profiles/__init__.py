"""Built-in semantic profiles."""

from .genai import PROFILE as GENAI_PROFILE
from .http import PROFILE as HTTP_PROFILE
from .mcp import PROFILE as MCP_PROFILE

__all__ = ["GENAI_PROFILE", "HTTP_PROFILE", "MCP_PROFILE"]
