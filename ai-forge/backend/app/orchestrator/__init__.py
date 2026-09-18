from __future__ import annotations

from app.providers.base import BaseModelProvider, ProviderHealth


class NVIDIAProvider(BaseModelProvider):
    provider_name = "nvidia"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, True, "connected", "NVIDIA API reachable")

    async def list_models(self) -> list[dict]:
        return [{"id": "meta/llama-3.1-70b-instruct", "capabilities": ["coding", "reasoning"]}]

    async def generate(self, prompt: str, **kwargs) -> dict:
        return {"provider": "nvidia", "prompt": prompt, "response": "NVIDIA model response placeholder"}


class OpenRouterProvider(BaseModelProvider):
    provider_name = "openrouter"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, True, "connected", "OpenRouter accessible")

    async def list_models(self) -> list[dict]:
        return [{"id": "openai/gpt-4o-mini", "capabilities": ["reasoning", "vision"]}]

    async def generate(self, prompt: str, **kwargs) -> dict:
        return {"provider": "openrouter", "prompt": prompt, "response": "OpenRouter model response placeholder"}


class LocalNIMProvider(BaseModelProvider):
    provider_name = "local_nim"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, False, "offline", "Local NIM endpoint unavailable")

    async def list_models(self) -> list[dict]:
        return [{"id": "local-llm", "capabilities": ["coding"]}]

    async def generate(self, prompt: str, **kwargs) -> dict:
        return {"provider": "local_nim", "prompt": prompt, "response": "Local NIM response placeholder"}


def get_provider(name: str, api_key: str = "", base_url: str = "") -> BaseModelProvider:
    providers = {
        "nvidia": NVIDIAProvider(api_key=api_key, base_url=base_url),
        "openrouter": OpenRouterProvider(api_key=api_key, base_url=base_url),
        "local_nim": LocalNIMProvider(api_key=api_key, base_url=base_url),
    }
    return providers.get(name.lower(), BaseModelProvider(api_key=api_key, base_url=base_url))


def list_providers() -> list[dict]:
    return [
        {"id": "nvidia", "name": "NVIDIA API", "status": "connected", "kind": "cloud"},
        {"id": "openrouter", "name": "OpenRouter", "status": "connected", "kind": "cloud"},
        {"id": "local_nim", "name": "Local NIM", "status": "offline", "kind": "local"},
    ]
