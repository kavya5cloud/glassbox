"""Registry and discovery helpers for provider adapters."""

from __future__ import annotations

from importlib import import_module
from pkgutil import iter_modules
from typing import Any

from .base import ProviderAdapter

_registered_adapters: list[type[ProviderAdapter]] = []
_discovered = False


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_register_adapter__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_register_adapter__mutmut)
def register_adapter(adapter: type[ProviderAdapter]) -> type[ProviderAdapter]:
    """Register a provider adapter class for later discovery."""
    if adapter not in _registered_adapters:
        _registered_adapters.append(adapter)
    return adapter


def x_register_adapter__mutmut_orig(adapter: type[ProviderAdapter]) -> type[ProviderAdapter]:
    """Register a provider adapter class for later discovery."""
    if adapter not in _registered_adapters:
        _registered_adapters.append(adapter)
    return adapter


def x_register_adapter__mutmut_1(adapter: type[ProviderAdapter]) -> type[ProviderAdapter]:
    """Register a provider adapter class for later discovery."""
    if adapter in _registered_adapters:
        _registered_adapters.append(adapter)
    return adapter


def x_register_adapter__mutmut_2(adapter: type[ProviderAdapter]) -> type[ProviderAdapter]:
    """Register a provider adapter class for later discovery."""
    if adapter not in _registered_adapters:
        _registered_adapters.append(None)
    return adapter

mutants_x_register_adapter__mutmut['_mutmut_orig'] = x_register_adapter__mutmut_orig # type: ignore # mutmut generated
mutants_x_register_adapter__mutmut['x_register_adapter__mutmut_1'] = x_register_adapter__mutmut_1 # type: ignore # mutmut generated
mutants_x_register_adapter__mutmut['x_register_adapter__mutmut_2'] = x_register_adapter__mutmut_2 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__discover_builtin_adapters__mutmut)
def _discover_builtin_adapters() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_orig() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_1() -> None:
    global _discovered
    if _discovered:
        return

    package = None
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_2() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module(None)
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_3() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("XXglassbox.providersXX")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_4() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("GLASSBOX.PROVIDERS")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_5() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(None, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_6() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, None):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_7() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_8() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, ):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_9() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ - "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_10() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "XX.XX"):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_11() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = None
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_12() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(None, 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_13() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", None)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_14() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_15() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", )[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_16() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.split(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_17() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit("XX.XX", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_18() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 2)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_19() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[+1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_20() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-2]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_21() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} and module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_22() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name not in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_23() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"XXbaseXX", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_24() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"BASE", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_25() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "XXmanagerXX", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_26() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "MANAGER", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_27() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "XXregistryXX"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_28() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "REGISTRY"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_29() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith(None):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_30() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("XX_XX"):
            continue
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_31() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            break
        import_module(module_info.name)

    _discovered = True


def x__discover_builtin_adapters__mutmut_32() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(None)

    _discovered = True


def x__discover_builtin_adapters__mutmut_33() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = None


def x__discover_builtin_adapters__mutmut_34() -> None:
    global _discovered
    if _discovered:
        return

    package = import_module("glassbox.providers")
    for module_info in iter_modules(package.__path__, package.__name__ + "."):
        module_name = module_info.name.rsplit(".", 1)[-1]
        if module_name in {"base", "manager", "registry"} or module_name.startswith("_"):
            continue
        import_module(module_info.name)

    _discovered = False

mutants_x__discover_builtin_adapters__mutmut['_mutmut_orig'] = x__discover_builtin_adapters__mutmut_orig # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_1'] = x__discover_builtin_adapters__mutmut_1 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_2'] = x__discover_builtin_adapters__mutmut_2 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_3'] = x__discover_builtin_adapters__mutmut_3 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_4'] = x__discover_builtin_adapters__mutmut_4 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_5'] = x__discover_builtin_adapters__mutmut_5 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_6'] = x__discover_builtin_adapters__mutmut_6 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_7'] = x__discover_builtin_adapters__mutmut_7 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_8'] = x__discover_builtin_adapters__mutmut_8 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_9'] = x__discover_builtin_adapters__mutmut_9 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_10'] = x__discover_builtin_adapters__mutmut_10 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_11'] = x__discover_builtin_adapters__mutmut_11 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_12'] = x__discover_builtin_adapters__mutmut_12 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_13'] = x__discover_builtin_adapters__mutmut_13 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_14'] = x__discover_builtin_adapters__mutmut_14 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_15'] = x__discover_builtin_adapters__mutmut_15 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_16'] = x__discover_builtin_adapters__mutmut_16 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_17'] = x__discover_builtin_adapters__mutmut_17 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_18'] = x__discover_builtin_adapters__mutmut_18 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_19'] = x__discover_builtin_adapters__mutmut_19 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_20'] = x__discover_builtin_adapters__mutmut_20 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_21'] = x__discover_builtin_adapters__mutmut_21 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_22'] = x__discover_builtin_adapters__mutmut_22 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_23'] = x__discover_builtin_adapters__mutmut_23 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_24'] = x__discover_builtin_adapters__mutmut_24 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_25'] = x__discover_builtin_adapters__mutmut_25 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_26'] = x__discover_builtin_adapters__mutmut_26 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_27'] = x__discover_builtin_adapters__mutmut_27 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_28'] = x__discover_builtin_adapters__mutmut_28 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_29'] = x__discover_builtin_adapters__mutmut_29 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_30'] = x__discover_builtin_adapters__mutmut_30 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_31'] = x__discover_builtin_adapters__mutmut_31 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_32'] = x__discover_builtin_adapters__mutmut_32 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_33'] = x__discover_builtin_adapters__mutmut_33 # type: ignore # mutmut generated
mutants_x__discover_builtin_adapters__mutmut['x__discover_builtin_adapters__mutmut_34'] = x__discover_builtin_adapters__mutmut_34 # type: ignore # mutmut generated
mutants_x_available_adapters__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_available_adapters__mutmut)
def available_adapters() -> tuple[type[ProviderAdapter], ...]:
    """Return all registered adapters, importing built-ins on first use."""
    _discover_builtin_adapters()
    return tuple(_registered_adapters)


def x_available_adapters__mutmut_orig() -> tuple[type[ProviderAdapter], ...]:
    """Return all registered adapters, importing built-ins on first use."""
    _discover_builtin_adapters()
    return tuple(_registered_adapters)


def x_available_adapters__mutmut_1() -> tuple[type[ProviderAdapter], ...]:
    """Return all registered adapters, importing built-ins on first use."""
    _discover_builtin_adapters()
    return tuple(None)

mutants_x_available_adapters__mutmut['_mutmut_orig'] = x_available_adapters__mutmut_orig # type: ignore # mutmut generated
mutants_x_available_adapters__mutmut['x_available_adapters__mutmut_1'] = x_available_adapters__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_adapter_for_client__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_adapter_for_client__mutmut)
def get_adapter_for_client(client: Any) -> type[ProviderAdapter] | None:
    """Return the first registered adapter that supports the given client."""
    for adapter in available_adapters():
        if adapter.supports(client):
            return adapter
    return None


def x_get_adapter_for_client__mutmut_orig(client: Any) -> type[ProviderAdapter] | None:
    """Return the first registered adapter that supports the given client."""
    for adapter in available_adapters():
        if adapter.supports(client):
            return adapter
    return None


def x_get_adapter_for_client__mutmut_1(client: Any) -> type[ProviderAdapter] | None:
    """Return the first registered adapter that supports the given client."""
    for adapter in available_adapters():
        if adapter.supports(None):
            return adapter
    return None

mutants_x_get_adapter_for_client__mutmut['_mutmut_orig'] = x_get_adapter_for_client__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_adapter_for_client__mutmut['x_get_adapter_for_client__mutmut_1'] = x_get_adapter_for_client__mutmut_1 # type: ignore # mutmut generated
