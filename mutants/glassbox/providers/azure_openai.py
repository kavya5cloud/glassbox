"""Azure OpenAI provider adapter stub."""

from __future__ import annotations

from typing import Any

from ._passthrough import PassThroughProviderAdapter
from .manager import register_adapter


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut: MutantDict = {}  # type: ignore


class AzureOpenAIAdapter(PassThroughProviderAdapter):
    """Adapter stub for Azure OpenAI clients."""

    provider_name = "Azure OpenAI"

    @classmethod
    @_mutmut_mutated(mutants_xǁAzureOpenAIAdapterǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_orig(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_1(cls, client: Any) -> bool:
        if hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_2(cls, client: Any) -> bool:
        if not hasattr(None, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_3(cls, client: Any) -> bool:
        if not hasattr(client, None):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_4(cls, client: Any) -> bool:
        if not hasattr("responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_5(cls, client: Any) -> bool:
        if not hasattr(client, ):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_6(cls, client: Any) -> bool:
        if not hasattr(client, "XXresponsesXX"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_7(cls, client: Any) -> bool:
        if not hasattr(client, "RESPONSES"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_8(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return True
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_9(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = None
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_10(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).upper()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_11(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            None
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_12(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") and ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_13(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) and getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_14(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(None, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_15(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, None, None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_16(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr("azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_17(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_18(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", ) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_19(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "XXazure_endpointXX", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_20(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "AZURE_ENDPOINT", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_21(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(None, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_22(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, None, "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_23(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", None) or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_24(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr("base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_25(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_26(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", ) or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_27(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "XXbase_urlXX", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_28(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "BASE_URL", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_29(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "XXXX") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_30(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or "XXXX"
        ).lower()
        return "azure" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_31(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint and hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_32(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "XXazureXX" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_33(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "AZURE" in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_34(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" not in endpoint or hasattr(client, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_35(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(None, "azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_36(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, None)

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_37(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr("azure_endpoint")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_38(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, )

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_39(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "XXazure_endpointXX")

    @classmethod
    def xǁAzureOpenAIAdapterǁsupports__mutmut_40(cls, client: Any) -> bool:
        if not hasattr(client, "responses"):
            return False
        endpoint = str(
            getattr(client, "azure_endpoint", None) or getattr(client, "base_url", "") or ""
        ).lower()
        return "azure" in endpoint or hasattr(client, "AZURE_ENDPOINT")

mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['_mutmut_orig'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_1'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_2'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_3'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_4'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_5'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_6'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_7'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_8'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_9'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_10'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_11'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_12'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_13'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_14'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_15'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_16'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_17'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_18'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_19'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_20'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_21'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_22'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_23'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_24'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_25'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_26'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_27'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_28'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_29'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_30'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_31'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_32'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_33'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_34'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_34 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_35'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_35 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_36'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_36 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_37'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_37 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_38'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_38 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_39'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_39 # type: ignore # mutmut generated
mutants_xǁAzureOpenAIAdapterǁsupports__mutmut['xǁAzureOpenAIAdapterǁsupports__mutmut_40'] = AzureOpenAIAdapter.xǁAzureOpenAIAdapterǁsupports__mutmut_40 # type: ignore # mutmut generated


register_adapter(AzureOpenAIAdapter)
