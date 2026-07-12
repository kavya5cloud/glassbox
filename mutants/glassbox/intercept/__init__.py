"""Interceptor helpers for wrapping provider clients."""

from __future__ import annotations

from typing import Any

from glassbox.providers.manager import get_adapter_for_client
from glassbox.tracing.bus import EventBus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_intercept__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_intercept__mutmut)
def intercept(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_orig(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_1(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is not None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_2(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = None

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_3(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = None
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_4(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(None)
    if adapter is not None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_5(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is None:
        return adapter.wrap(client, event_bus=event_bus)

    return client


def x_intercept__mutmut_6(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(None, event_bus=event_bus)

    return client


def x_intercept__mutmut_7(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, event_bus=None)

    return client


def x_intercept__mutmut_8(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(event_bus=event_bus)

    return client


def x_intercept__mutmut_9(client: Any, *, event_bus: EventBus | None = None) -> Any:
    """Wrap a provider client instance and publish trace events for requests."""
    if event_bus is None:
        from glassbox.tracing.bus import default_bus

        event_bus = default_bus

    adapter = get_adapter_for_client(client)
    if adapter is not None:
        return adapter.wrap(client, )

    return client

mutants_x_intercept__mutmut['_mutmut_orig'] = x_intercept__mutmut_orig # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_1'] = x_intercept__mutmut_1 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_2'] = x_intercept__mutmut_2 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_3'] = x_intercept__mutmut_3 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_4'] = x_intercept__mutmut_4 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_5'] = x_intercept__mutmut_5 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_6'] = x_intercept__mutmut_6 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_7'] = x_intercept__mutmut_7 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_8'] = x_intercept__mutmut_8 # type: ignore # mutmut generated
mutants_x_intercept__mutmut['x_intercept__mutmut_9'] = x_intercept__mutmut_9 # type: ignore # mutmut generated
