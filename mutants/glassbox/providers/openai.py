"""OpenAI client adapter for generating Glassbox traces."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from glassbox.providers.manager import register_adapter
from glassbox.tracing import EventBus
from glassbox.tracing.builder import TraceBuilder
from glassbox.tracing.bus import default_bus


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁOpenAIInterceptorǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIInterceptorǁsupports__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIInterceptorǁwrap__mutmut: MutantDict = {}  # type: ignore


class OpenAIInterceptor:
    """Wrap an OpenAI client instance and publish traces for responses.create calls."""

    provider_name = "OpenAI"

    @_mutmut_mutated(mutants_xǁOpenAIInterceptorǁ__init____mutmut)
    def __init__(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_orig(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_1(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = None
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_2(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = None
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_3(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus and default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_4(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = None
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_5(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=None)
        self.responses = OpenAIResponsesAdapter(client.responses, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_6(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = None

    def xǁOpenAIInterceptorǁ__init____mutmut_7(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(None, self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_8(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, None)

    def xǁOpenAIInterceptorǁ__init____mutmut_9(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(self._builder)

    def xǁOpenAIInterceptorǁ__init____mutmut_10(self, client: Any, event_bus: EventBus | None = None) -> None:
        self._client = client
        self._event_bus = event_bus or default_bus
        self._builder = TraceBuilder(event_bus=self._event_bus)
        self.responses = OpenAIResponsesAdapter(client.responses, )

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenAIInterceptorǁsupports__mutmut, is_classmethod = True)
    def supports(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_orig(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_1(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_2(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(None, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_3(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, None):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_4(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr("responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_5(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, ):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_6(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "XXresponsesXX"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_7(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "RESPONSES"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_8(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return True
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_9(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = None
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_10(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").upper()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_11(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(None).lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_12(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") and "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_13(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(None, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_14(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, None, "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_15(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", None) or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_16(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr("base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_17(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_18(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", ) or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_19(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "XXbase_urlXX", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_20(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "BASE_URL", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_21(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "XXXX") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_22(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "XXXX").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_23(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url and "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_24(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "XXopenrouterXX" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_25(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "OPENROUTER" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_26(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" not in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_27(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "XXazureXX" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_28(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "AZURE" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_29(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" not in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_30(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return True
        if hasattr(client, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_31(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(None, "azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_32(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, None):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_33(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr("azure_endpoint"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_34(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, ):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_35(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "XXazure_endpointXX"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_36(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "AZURE_ENDPOINT"):
            return False
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_37(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return True
        return True

    @classmethod
    def xǁOpenAIInterceptorǁsupports__mutmut_38(cls, client: Any) -> bool:
        """Return ``True`` for OpenAI-compatible clients."""
        if not hasattr(client, "responses"):
            return False
        base_url = str(getattr(client, "base_url", "") or "").lower()
        if "openrouter" in base_url or "azure" in base_url:
            return False
        if hasattr(client, "azure_endpoint"):
            return False
        return False

    @classmethod
    @_mutmut_mutated(mutants_xǁOpenAIInterceptorǁwrap__mutmut, is_classmethod = True)
    def wrap(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(client, event_bus=event_bus)

    @classmethod
    def xǁOpenAIInterceptorǁwrap__mutmut_orig(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(client, event_bus=event_bus)

    @classmethod
    def xǁOpenAIInterceptorǁwrap__mutmut_1(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(None, event_bus=event_bus)

    @classmethod
    def xǁOpenAIInterceptorǁwrap__mutmut_2(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(client, event_bus=None)

    @classmethod
    def xǁOpenAIInterceptorǁwrap__mutmut_3(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(event_bus=event_bus)

    @classmethod
    def xǁOpenAIInterceptorǁwrap__mutmut_4(cls, client: Any, *, event_bus: EventBus | None = None) -> Any:
        """Return a wrapped client instance."""
        return cls(client, )

mutants_xǁOpenAIInterceptorǁ__init____mutmut['_mutmut_orig'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_1'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_2'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_3'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_4'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_5'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_6'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_7'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_8'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_9'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁ__init____mutmut['xǁOpenAIInterceptorǁ__init____mutmut_10'] = OpenAIInterceptor.xǁOpenAIInterceptorǁ__init____mutmut_10 # type: ignore # mutmut generated

mutants_xǁOpenAIInterceptorǁsupports__mutmut['_mutmut_orig'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_1'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_2'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_3'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_4'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_5'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_6'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_7'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_8'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_9'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_10'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_11'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_12'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_13'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_14'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_15'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_16'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_17'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_18'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_19'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_20'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_21'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_22'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_23'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_24'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_25'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_26'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_27'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_28'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_29'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_30'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_31'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_32'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_33'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_34'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_35'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_36'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_37'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁsupports__mutmut['xǁOpenAIInterceptorǁsupports__mutmut_38'] = OpenAIInterceptor.xǁOpenAIInterceptorǁsupports__mutmut_38 # type: ignore # mutmut generated

mutants_xǁOpenAIInterceptorǁwrap__mutmut['_mutmut_orig'] = OpenAIInterceptor.xǁOpenAIInterceptorǁwrap__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁwrap__mutmut['xǁOpenAIInterceptorǁwrap__mutmut_1'] = OpenAIInterceptor.xǁOpenAIInterceptorǁwrap__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁwrap__mutmut['xǁOpenAIInterceptorǁwrap__mutmut_2'] = OpenAIInterceptor.xǁOpenAIInterceptorǁwrap__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁwrap__mutmut['xǁOpenAIInterceptorǁwrap__mutmut_3'] = OpenAIInterceptor.xǁOpenAIInterceptorǁwrap__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIInterceptorǁwrap__mutmut['xǁOpenAIInterceptorǁwrap__mutmut_4'] = OpenAIInterceptor.xǁOpenAIInterceptorǁwrap__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut: MutantDict = {}  # type: ignore
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut: MutantDict = {}  # type: ignore


class OpenAIResponsesAdapter:
    """Adapter for the OpenAI responses API."""

    @_mutmut_mutated(mutants_xǁOpenAIResponsesAdapterǁ__init____mutmut)
    def __init__(self, client: Any, builder: TraceBuilder) -> None:
        self._client = client
        self._builder = builder

    def xǁOpenAIResponsesAdapterǁ__init____mutmut_orig(self, client: Any, builder: TraceBuilder) -> None:
        self._client = client
        self._builder = builder

    def xǁOpenAIResponsesAdapterǁ__init____mutmut_1(self, client: Any, builder: TraceBuilder) -> None:
        self._client = None
        self._builder = builder

    def xǁOpenAIResponsesAdapterǁ__init____mutmut_2(self, client: Any, builder: TraceBuilder) -> None:
        self._client = client
        self._builder = None

    @_mutmut_mutated(mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut)
    def create(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_orig(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_1(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = None
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_2(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(None)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_3(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = None
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_4(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(None)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_5(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = None
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_6(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(**kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_7(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, )
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_8(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = None
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_9(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(None)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_10(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = None
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_11(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") and getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_12(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get(None) or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_13(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("XXmodelXX") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_14(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("MODEL") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_15(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(None, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_16(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, None, "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_17(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", None)
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_18(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr("model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_19(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_20(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", )
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_21(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "XXmodelXX", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_22(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "MODEL", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_23(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "XXunknownXX")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_24(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "UNKNOWN")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_25(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_26(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = None
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_27(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "XXunknownXX"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_28(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "UNKNOWN"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_29(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = None
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_30(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider=None,
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_31(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=None,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_32(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=None,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_33(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=None,
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_34(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=None,
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_35(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=None,
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_36(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=None,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_37(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=None,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_38(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status=None,
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_39(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_40(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_41(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_42(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_43(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_44(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_45(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_46(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_47(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_48(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="XXOpenAIXX",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_49(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="openai",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_50(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OPENAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_51(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(None),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_52(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(None, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_53(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, None),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_54(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value("input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_55(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, ),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_56(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "XXinput_tokensXX"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_57(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "INPUT_TOKENS"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_58(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(None, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_59(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, None),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_60(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value("output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_61(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, ),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_62(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "XXoutput_tokensXX"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_63(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "OUTPUT_TOKENS"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_64(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="XXcompletedXX",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_65(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="COMPLETED",
        )
        self._builder.publish(trace)
        return response

    def xǁOpenAIResponsesAdapterǁcreate__mutmut_66(self, *args: Any, **kwargs: Any) -> Any:
        """Create a response and publish a trace when it completes."""
        started_at = datetime.now(timezone.utc)
        request_text = self._extract_request_text(kwargs)
        response = self._client.create(*args, **kwargs)
        ended_at = datetime.now(timezone.utc)
        model = kwargs.get("model") or getattr(response, "model", "unknown")
        if not isinstance(model, str):
            model = "unknown"
        trace = self._builder.build(
            provider="OpenAI",
            model=model,
            prompt=request_text,
            response_text=self._extract_response_text(response),
            input_tokens=self._extract_usage_value(response, "input_tokens"),
            output_tokens=self._extract_usage_value(response, "output_tokens"),
            started_at=started_at,
            ended_at=ended_at,
            status="completed",
        )
        self._builder.publish(None)
        return response

    @_mutmut_mutated(mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut)
    def _extract_request_text(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_orig(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_1(self, kwargs: dict[str, Any]) -> str:
        if "XXinputXX" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_2(self, kwargs: dict[str, Any]) -> str:
        if "INPUT" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_3(self, kwargs: dict[str, Any]) -> str:
        if "input" not in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_4(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = None
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_5(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["XXinputXX"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_6(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["INPUT"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_7(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = None
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_8(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = None
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_9(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get(None)
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_10(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("XXtextXX")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_11(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("TEXT")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_12(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(None)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_13(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(None)
                if parts:
                    return "\n".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_14(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(None)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_15(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "XX\nXX".join(parts)
        return ""

    def xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_16(self, kwargs: dict[str, Any]) -> str:
        if "input" in kwargs:
            value = kwargs["input"]
            if isinstance(value, str):
                return value
            if isinstance(value, list):
                parts: list[str] = []
                for item in value:
                    if isinstance(item, dict):
                        text = item.get("text")
                        if isinstance(text, str):
                            parts.append(text)
                    elif isinstance(item, str):
                        parts.append(item)
                if parts:
                    return "\n".join(parts)
        return "XXXX"

    @_mutmut_mutated(mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut)
    def _extract_response_text(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_orig(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_1(self, response: Any) -> str:
        output = None
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_2(self, response: Any) -> str:
        output = getattr(None, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_3(self, response: Any) -> str:
        output = getattr(response, None, None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_4(self, response: Any) -> str:
        output = getattr("output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_5(self, response: Any) -> str:
        output = getattr(response, None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_6(self, response: Any) -> str:
        output = getattr(response, "output", )
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_7(self, response: Any) -> str:
        output = getattr(response, "XXoutputXX", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_8(self, response: Any) -> str:
        output = getattr(response, "OUTPUT", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_9(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_10(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return "XXXX"
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_11(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = None
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_12(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = None
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_13(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) and []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_14(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(None, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_15(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, None, None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_16(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr("content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_17(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_18(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", ) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_19(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "XXcontentXX", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_20(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "CONTENT", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_21(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = None
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_22(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(None, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_23(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, None, None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_24(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr("text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_25(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_26(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", )
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_27(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "XXtextXX", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_28(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "TEXT", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_29(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(None)
        return "\n".join(texts)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_30(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "\n".join(None)

    def xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_31(self, response: Any) -> str:
        output = getattr(response, "output", None)
        if not output:
            return ""
        texts: list[str] = []
        for item in output:
            content = getattr(item, "content", None) or []
            for part in content:
                text = getattr(part, "text", None)
                if isinstance(text, str):
                    texts.append(text)
        return "XX\nXX".join(texts)

    @_mutmut_mutated(mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut)
    def _extract_usage_value(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_orig(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_1(self, response: Any, field: str) -> int:
        usage = None
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_2(self, response: Any, field: str) -> int:
        usage = getattr(None, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_3(self, response: Any, field: str) -> int:
        usage = getattr(response, None, None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_4(self, response: Any, field: str) -> int:
        usage = getattr("usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_5(self, response: Any, field: str) -> int:
        usage = getattr(response, None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_6(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", )
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_7(self, response: Any, field: str) -> int:
        usage = getattr(response, "XXusageXX", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_8(self, response: Any, field: str) -> int:
        usage = getattr(response, "USAGE", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_9(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is not None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_10(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 1
        value = getattr(usage, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_11(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = None
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_12(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(None, field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_13(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, None, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_14(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(field, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_15(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, None)
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_16(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, )
        return int(value or 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_17(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(None)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_18(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value and 0)

    def xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_19(self, response: Any, field: str) -> int:
        usage = getattr(response, "usage", None)
        if usage is None:
            return 0
        value = getattr(usage, field, None)
        return int(value or 1)

mutants_xǁOpenAIResponsesAdapterǁ__init____mutmut['_mutmut_orig'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ__init____mutmut['xǁOpenAIResponsesAdapterǁ__init____mutmut_1'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ__init____mutmut['xǁOpenAIResponsesAdapterǁ__init____mutmut_2'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['_mutmut_orig'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_1'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_2'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_3'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_4'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_5'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_6'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_7'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_8'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_9'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_10'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_11'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_12'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_13'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_14'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_15'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_16'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_17'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_18'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_19'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_20'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_21'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_22'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_23'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_24'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_25'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_26'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_27'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_28'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_29'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_30'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_31'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_31 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_32'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_32 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_33'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_33 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_34'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_34 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_35'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_35 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_36'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_36 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_37'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_37 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_38'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_38 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_39'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_39 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_40'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_40 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_41'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_41 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_42'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_42 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_43'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_43 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_44'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_44 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_45'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_45 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_46'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_46 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_47'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_47 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_48'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_48 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_49'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_49 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_50'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_50 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_51'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_51 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_52'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_52 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_53'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_53 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_54'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_54 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_55'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_55 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_56'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_56 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_57'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_57 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_58'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_58 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_59'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_59 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_60'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_60 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_61'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_61 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_62'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_62 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_63'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_63 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_64'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_64 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_65'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_65 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁcreate__mutmut['xǁOpenAIResponsesAdapterǁcreate__mutmut_66'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁcreate__mutmut_66 # type: ignore # mutmut generated

mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['_mutmut_orig'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_1'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_2'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_3'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_4'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_5'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_6'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_7'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_8'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_9'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_10'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_11'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_12'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_13'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_14'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_15'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_16'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_request_text__mutmut_16 # type: ignore # mutmut generated

mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['_mutmut_orig'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_1'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_2'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_3'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_4'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_5'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_6'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_7'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_8'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_9'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_10'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_11'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_12'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_13'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_14'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_15'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_16'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_17'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_18'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_19'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_19 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_20'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_20 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_21'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_21 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_22'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_22 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_23'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_23 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_24'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_24 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_25'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_25 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_26'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_26 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_27'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_27 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_28'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_28 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_29'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_29 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_30'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_30 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut['xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_31'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_response_text__mutmut_31 # type: ignore # mutmut generated

mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['_mutmut_orig'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_orig # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_1'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_1 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_2'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_2 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_3'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_3 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_4'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_4 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_5'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_5 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_6'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_6 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_7'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_7 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_8'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_8 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_9'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_9 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_10'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_10 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_11'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_11 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_12'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_12 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_13'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_13 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_14'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_14 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_15'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_15 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_16'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_16 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_17'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_17 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_18'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_18 # type: ignore # mutmut generated
mutants_xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut['xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_19'] = OpenAIResponsesAdapter.xǁOpenAIResponsesAdapterǁ_extract_usage_value__mutmut_19 # type: ignore # mutmut generated


register_adapter(OpenAIInterceptor)
