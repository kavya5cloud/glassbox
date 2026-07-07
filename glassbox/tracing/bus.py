"""A lightweight publish-subscribe event bus for traces."""

from __future__ import annotations

from threading import Lock
from typing import Callable, TypeAlias

from .trace import Trace

Subscriber: TypeAlias = Callable[[Trace], None]


class EventBus:
    """Simple thread-safe event bus for publishing trace events."""

    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []
        self._lock = Lock()

    def subscribe(self, callback: Subscriber) -> None:
        """Register a callback to receive published traces."""
        with self._lock:
            if callback not in self._subscribers:
                self._subscribers.append(callback)

    def publish(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = list(self._subscribers)

        for callback in subscribers:
            callback(trace)


default_bus = EventBus()
