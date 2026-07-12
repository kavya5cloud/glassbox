"""Anthropic provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAnthropicAdapterǁsupports__mutmut: MutantDict = {}  # type: ignore


class AnthropicAdapter(PassThroughProviderAdapter):
    """Adapter stub for Anthropic clients."""

    provider_name = "Anthropic"

    @classmethod
    @_mutmut_mutated(mutants_xǁAnthropicAdapterǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "messages")

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_orig(cls, client: Any) -> bool:
        return hasattr(client, "messages")

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_1(cls, client: Any) -> bool:
        return hasattr(None, "messages")

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_2(cls, client: Any) -> bool:
        return hasattr(client, None)

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_3(cls, client: Any) -> bool:
        return hasattr("messages")

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_4(cls, client: Any) -> bool:
        return hasattr(client, )

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_5(cls, client: Any) -> bool:
        return hasattr(client, "XXmessagesXX")

    @classmethod
    def xǁAnthropicAdapterǁsupports__mutmut_6(cls, client: Any) -> bool:
        return hasattr(client, "MESSAGES")

mutants_xǁAnthropicAdapterǁsupports__mutmut['_mutmut_orig'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_1'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_2'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_3'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_4'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_5'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAnthropicAdapterǁsupports__mutmut['xǁAnthropicAdapterǁsupports__mutmut_6'] = AnthropicAdapter.xǁAnthropicAdapterǁsupports__mutmut_6 # type: ignore # mutmut generated


register_adapter(AnthropicAdapter)
