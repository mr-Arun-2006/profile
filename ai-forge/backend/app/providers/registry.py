from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderHealth:
    name: str
    connected: bool
    status: str
    details: str | None = None


class BaseModelProvider:
    """Common provider contract for all model backends."""

    provider_name: str = "base"

    def __init__(self, api_key: str = "", base_url: str = "") -> None:
        self.api_key = api_key
        self.base_url = base_url

    async def test_connection(self) -> ProviderHealth:
        return ProviderHealth(self.provider_name, True, "connected")

    async def list_models(self) -> list[dict[str, Any]]:
        return []

    async def generate(self, prompt: str, **kwargs: Any) -> dict[str, Any]:
        raise NotImplementedError("Provider must implement generate().")
