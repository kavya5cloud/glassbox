"""Function decorators built on the SDK core.

Public API:
- sessionized

Future extension points:
- observation capture wrappers
- evaluation hooks
- execution tagging
"""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

from glassbox.core import Session

from .api import Glassbox

P = ParamSpec("P")
T = TypeVar("T")


def sessionized(
    sdk: Glassbox,
    *,
    session_id: str | None = None,
) -> Callable[[Callable[P, T]], Callable[P, tuple[T, Session]]]:
    """Wrap a function and return its result plus a session record.

    The decorator is intentionally small. It gives the SDK a stable extension
    point for future instrumentation without forcing capture or transport
    concerns into the core API.
    """

    def decorate(fn: Callable[P, T]) -> Callable[P, tuple[T, Session]]:
        @wraps(fn)
        def wrapped(*args: P.args, **kwargs: P.kwargs) -> tuple[T, Session]:
            context = sdk.open_session(session_id or fn.__qualname__)
            if context.session is None:
                raise RuntimeError("session could not be opened")
            return fn(*args, **kwargs), context.session

        return wrapped

    return decorate
