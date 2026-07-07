from collections.abc import Callable
from typing import Any


class EventBus:
    def __init__(self):
        self._listeners: list[Callable[[Any], None]] = []

    def subscribe(self, callback: Callable[[Any], None]):
        self._listeners.append(callback)

    def publish(self, event):
        for listener in self._listeners:
            listener(event)