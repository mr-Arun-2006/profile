from __future__ import annotations

from typing import Any

from app.providers.base import BaseModelProvider, ProviderHealth


class NVIDIAProvider(BaseModelProvider):
    provider_name = "nvidia"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, True, "connected", "NVIDIA API reachable")

    async def list_models(self) -> list[dict[str, Any]]:
        return [{"id": "meta/llama-3.1-70b-instruct", "capabilities": ["coding", "reasoning"], "status": "online"}]

    async def generate(self, prompt: str, **kwargs: Any) -> dict[str, Any]:
        return {"provider": "nvidia", "prompt": prompt, "response": "NVIDIA model response placeholder"}


class OpenRouterProvider(BaseModelProvider):
    provider_name = "openrouter"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, True, "connected", "OpenRouter accessible")

    async def list_models(self) -> list[dict[str, Any]]:
        return [{"id": "openai/gpt-4o-mini", "capabilities": ["reasoning", "vision"], "status": "online"}]

    async def generate(self, prompt: str, **kwargs: Any) -> dict[str, Any]:
        return {"provider": "openrouter", "prompt": prompt, "response": "OpenRouter model response placeholder"}


class LocalNIMProvider(BaseModelProvider):
    provider_name = "local_nim"

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, False, "offline", "Local NIM endpoint unavailable")

    async def list_models(self) -> list[dict[str, Any]]:
        return [{"id": "local-llm", "capabilities": ["coding"], "status": "offline"}]

    async def generate(self, prompt: str, **kwargs: Any) -> dict[str, Any]:
        return {"provider": "local_nim", "prompt": prompt, "response": "Local NIM response placeholder"}


PROVIDER_REGISTRY = {
    "nvidia": NVIDIAProvider,
    "openrouter": OpenRouterProvider,
    "local_nim": LocalNIMProvider,
}


def get_provider(name: str, api_key: str = "", base_url: str = "") -> BaseModelProvider:
    provider_cls = PROVIDER_REGISTRY.get(name.lower(), BaseModelProvider)
    return provider_cls(api_key=api_key, base_url=base_url)


def list_providers() -> list[dict[str, Any]]:
    return [
        {"id": "nvidia", "name": "NVIDIA API", "status": "connected", "kind": "cloud", "api_key_masked": "********"},
        {"id": "openrouter", "name": "OpenRouter", "status": "connected", "kind": "cloud", "api_key_masked": "********"},
        {"id": "local_nim", "name": "Local NIM", "status": "offline", "kind": "local", "endpoint": "http://localhost:8000/v1"},
    ]
