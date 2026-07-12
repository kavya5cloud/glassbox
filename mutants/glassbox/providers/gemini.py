"""Gemini provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁGeminiAdapterǁsupports__mutmut: MutantDict = {}  # type: ignore


class GeminiAdapter(PassThroughProviderAdapter):
    """Adapter stub for Gemini clients."""

    provider_name = "Gemini"

    @classmethod
    @_mutmut_mutated(mutants_xǁGeminiAdapterǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_orig(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_1(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") and hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_2(cls, client: Any) -> bool:
        return hasattr(None, "generate_content") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_3(cls, client: Any) -> bool:
        return hasattr(client, None) or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_4(cls, client: Any) -> bool:
        return hasattr("generate_content") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_5(cls, client: Any) -> bool:
        return hasattr(client, ) or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_6(cls, client: Any) -> bool:
        return hasattr(client, "XXgenerate_contentXX") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_7(cls, client: Any) -> bool:
        return hasattr(client, "GENERATE_CONTENT") or hasattr(client, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_8(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(None, "models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_9(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, None)

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_10(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr("models")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_11(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, )

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_12(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, "XXmodelsXX")

    @classmethod
    def xǁGeminiAdapterǁsupports__mutmut_13(cls, client: Any) -> bool:
        return hasattr(client, "generate_content") or hasattr(client, "MODELS")

mutants_xǁGeminiAdapterǁsupports__mutmut['_mutmut_orig'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_1'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_2'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_3'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_4'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_5'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_6'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_7'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_8'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_9'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_10'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_11'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_12'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGeminiAdapterǁsupports__mutmut['xǁGeminiAdapterǁsupports__mutmut_13'] = GeminiAdapter.xǁGeminiAdapterǁsupports__mutmut_13 # type: ignore # mutmut generated


register_adapter(GeminiAdapter)
