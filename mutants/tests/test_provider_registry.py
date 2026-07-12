from __future__ import annotations

from types import SimpleNamespace

from glassbox.providers.manager import available_adapters, get_adapter_for_client


class FakeOpenAIClient:
    def __init__(self) -> None:
        self.responses = SimpleNamespace()


class FakeAnthropicClient:
    def __init__(self) -> None:
        self.messages = SimpleNamespace()


class FakeGeminiClient:
    def __init__(self) -> None:
        self.generate_content = SimpleNamespace()


class FakeAzureOpenAIClient:
    def __init__(self) -> None:
        self.responses = SimpleNamespace()
        self.azure_endpoint = "https://example.openai.azure.com/"


class FakeOllamaClient:
    def __init__(self) -> None:
        self.chat = SimpleNamespace()


class FakeOpenRouterClient:
    def __init__(self) -> None:
        self.responses = SimpleNamespace()
        self.base_url = "https://openrouter.ai/api/v1"


def test_provider_registry_discovers_builtin_adapters() -> None:
    adapters = available_adapters()
    provider_names = {adapter.provider_name for adapter in adapters}

    assert provider_names == {
        "OpenAI",
        "Anthropic",
        "Gemini",
        "Azure OpenAI",
        "Ollama",
        "OpenRouter",
    }


def test_provider_registry_selects_matching_adapter_for_each_client_shape() -> None:
    cases = [
        (FakeOpenAIClient(), "OpenAI"),
        (FakeAnthropicClient(), "Anthropic"),
        (FakeGeminiClient(), "Gemini"),
        (FakeAzureOpenAIClient(), "Azure OpenAI"),
        (FakeOllamaClient(), "Ollama"),
        (FakeOpenRouterClient(), "OpenRouter"),
    ]

    for client, expected_provider_name in cases:
        adapter = get_adapter_for_client(client)
        assert adapter is not None
        assert adapter.provider_name == expected_provider_name
