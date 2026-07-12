"""OpenRouter provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenRouterAdapterǁsupports__mutmut: MutantDict = {}  # type: ignore


class OpenRouterAdapter(PassThroughProviderAdapter):
    """Adapter stub for OpenRouter clients."""

    provider_name = "OpenRouter"

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenRouterAdapterǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_orig(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_1(cls, client: Any) -> bool:
        if hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_2(cls, client: Any) -> bool:
        if not hasattr(None, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_3(cls, client: Any) -> bool:
        if not hasattr(client, None):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_4(cls, client: Any) -> bool:
        if not hasattr("responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_5(cls, client: Any) -> bool:
        if not hasattr(client, ):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_6(cls, client: Any) -> bool:
        if not hasattr(client, "XXresponsesXX"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_7(cls, client: Any) -> bool:
        if not hasattr(client, "RESPONSES"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_8(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return True
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_9(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = None
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_10(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(None, "base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_11(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, None, "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_12(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", None)
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_13(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr("base_url", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_14(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_15(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", )
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_16(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "XXbase_urlXX", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_17(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "BASE_URL", "")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_18(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "XXXX")
        return "openrouter" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_19(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "XXopenrouterXX" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_20(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "OPENROUTER" in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_21(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" not in str(base_url).lower()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_22(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(base_url).upper()

    @classmethod
    def xǁOpenRouterAdapterǁsupports__mutmut_23(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        base_url = getattr(client, "base_url", "")
        return "openrouter" in str(None).lower()

mutants_xǁOpenRouterAdapterǁsupports__mutmut['_mutmut_orig'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_1'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_2'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_3'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_4'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_5'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_6'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_7'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_8'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_9'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_10'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_11'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_12'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_13'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_14'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_15'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_16'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_17'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_18'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_19'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_20'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_21'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_22'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOpenRouterAdapterǁsupports__mutmut['xǁOpenRouterAdapterǁsupports__mutmut_23'] = OpenRouterAdapter.xǁOpenRouterAdapterǁsupports__mutmut_23 # type: ignore # mutmut generated


register_adapter(OpenRouterAdapter)
