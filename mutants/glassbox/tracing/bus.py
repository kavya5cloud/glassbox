"""A lightweight publish-subscribe event bus for traces."""

from __future__ import annotations

from collections.abc import Callable
from threading import Lock
from typing import TypeAlias

from .trace import Trace

Subscriber: TypeAlias = Callable[[Trace], None]


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁEventBusǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁEventBusǁsubscribe__mutmut: MutantDict = {}  # type: ignore
mutants_xǁEventBusǁpublish__mutmut: MutantDict = {}  # type: ignore


class EventBus:
    """Simple thread-safe event bus for publishing trace events."""

    @_mutmut_mutated(mutants_xǁEventBusǁ__init____mutmut)
    def __init__(self) -> None:
        self._subscribers: list[Subscriber] = []
        self._lock = Lock()

    def xǁEventBusǁ__init____mutmut_orig(self) -> None:
        self._subscribers: list[Subscriber] = []
        self._lock = Lock()

    def xǁEventBusǁ__init____mutmut_1(self) -> None:
        self._subscribers: list[Subscriber] = None
        self._lock = Lock()

    def xǁEventBusǁ__init____mutmut_2(self) -> None:
        self._subscribers: list[Subscriber] = []
        self._lock = None

    @_mutmut_mutated(mutants_xǁEventBusǁsubscribe__mutmut)
    def subscribe(self, callback: Subscriber) -> None:
        """Register a callback to receive published traces."""
        with self._lock:
            if callback not in self._subscribers:
                self._subscribers.append(callback)

    def xǁEventBusǁsubscribe__mutmut_orig(self, callback: Subscriber) -> None:
        """Register a callback to receive published traces."""
        with self._lock:
            if callback not in self._subscribers:
                self._subscribers.append(callback)

    def xǁEventBusǁsubscribe__mutmut_1(self, callback: Subscriber) -> None:
        """Register a callback to receive published traces."""
        with self._lock:
            if callback in self._subscribers:
                self._subscribers.append(callback)

    def xǁEventBusǁsubscribe__mutmut_2(self, callback: Subscriber) -> None:
        """Register a callback to receive published traces."""
        with self._lock:
            if callback not in self._subscribers:
                self._subscribers.append(None)

    @_mutmut_mutated(mutants_xǁEventBusǁpublish__mutmut)
    def publish(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = list(self._subscribers)

        for callback in subscribers:
            callback(trace)

    def xǁEventBusǁpublish__mutmut_orig(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = list(self._subscribers)

        for callback in subscribers:
            callback(trace)

    def xǁEventBusǁpublish__mutmut_1(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = None

        for callback in subscribers:
            callback(trace)

    def xǁEventBusǁpublish__mutmut_2(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = list(None)

        for callback in subscribers:
            callback(trace)

    def xǁEventBusǁpublish__mutmut_3(self, trace: Trace) -> None:
        """Publish a trace to all subscribed callbacks."""
        with self._lock:
            subscribers = list(self._subscribers)

        for callback in subscribers:
            callback(None)

mutants_xǁEventBusǁ__init____mutmut['_mutmut_orig'] = EventBus.xǁEventBusǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventBusǁ__init____mutmut['xǁEventBusǁ__init____mutmut_1'] = EventBus.xǁEventBusǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventBusǁ__init____mutmut['xǁEventBusǁ__init____mutmut_2'] = EventBus.xǁEventBusǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁEventBusǁsubscribe__mutmut['_mutmut_orig'] = EventBus.xǁEventBusǁsubscribe__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventBusǁsubscribe__mutmut['xǁEventBusǁsubscribe__mutmut_1'] = EventBus.xǁEventBusǁsubscribe__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventBusǁsubscribe__mutmut['xǁEventBusǁsubscribe__mutmut_2'] = EventBus.xǁEventBusǁsubscribe__mutmut_2 # type: ignore # mutmut generated

mutants_xǁEventBusǁpublish__mutmut['_mutmut_orig'] = EventBus.xǁEventBusǁpublish__mutmut_orig # type: ignore # mutmut generated
mutants_xǁEventBusǁpublish__mutmut['xǁEventBusǁpublish__mutmut_1'] = EventBus.xǁEventBusǁpublish__mutmut_1 # type: ignore # mutmut generated
mutants_xǁEventBusǁpublish__mutmut['xǁEventBusǁpublish__mutmut_2'] = EventBus.xǁEventBusǁpublish__mutmut_2 # type: ignore # mutmut generated
mutants_xǁEventBusǁpublish__mutmut['xǁEventBusǁpublish__mutmut_3'] = EventBus.xǁEventBusǁpublish__mutmut_3 # type: ignore # mutmut generated


default_bus = EventBus()
