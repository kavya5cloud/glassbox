"""Ollama provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOllamaAdapterǁsupports__mutmut: MutantDict = {}  # type: ignore


class OllamaAdapter(PassThroughProviderAdapter):
    """Adapter stub for Ollama clients."""

    provider_name = "Ollama"

    @classmethod
    @_mutmut_mutated(mutants_xǁOllamaAdapterǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_orig(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_1(cls, client: Any) -> bool:
        return hasattr(client, "chat") and hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_2(cls, client: Any) -> bool:
        return hasattr(None, "chat") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_3(cls, client: Any) -> bool:
        return hasattr(client, None) or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_4(cls, client: Any) -> bool:
        return hasattr("chat") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_5(cls, client: Any) -> bool:
        return hasattr(client, ) or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_6(cls, client: Any) -> bool:
        return hasattr(client, "XXchatXX") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_7(cls, client: Any) -> bool:
        return hasattr(client, "CHAT") or hasattr(client, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_8(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(None, "generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_9(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, None)

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_10(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr("generate")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_11(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, )

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_12(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, "XXgenerateXX")

    @classmethod
    def xǁOllamaAdapterǁsupports__mutmut_13(cls, client: Any) -> bool:
        return hasattr(client, "chat") or hasattr(client, "GENERATE")

mutants_xǁOllamaAdapterǁsupports__mutmut['_mutmut_orig'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_1'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_2'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_3'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_4'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_5'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_6'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_7'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_8'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_9'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_10'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_11'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_12'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOllamaAdapterǁsupports__mutmut['xǁOllamaAdapterǁsupports__mutmut_13'] = OllamaAdapter.xǁOllamaAdapterǁsupports__mutmut_13 # type: ignore # mutmut generated


register_adapter(OllamaAdapter)
