"""Thin REST client for the Foundry IQ (Azure AI Search) data plane.

Uses REST instead of the preview SDK so every request body stays visible and matches
the Microsoft Learn examples one to one.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import httpx
from azure.identity import DefaultAzureCredential

from .config import get_settings

ROOT = Path(__file__).resolve().parents[2]

SEARCH_SCOPE = "https://search.azure.com/.default"


@lru_cache(maxsize=1)
def credential() -> DefaultAzureCredential:
    """One credential for the whole process: it caches tokens, so every client shares it."""
    return DefaultAzureCredential()


@dataclass
class Settings:
    """The Azure settings a client needs, defaulting to config.py (one source of truth)."""

    search_endpoint: str = field(default_factory=lambda: get_settings().search_endpoint.rstrip("/"))
    api_version: str = field(default_factory=lambda: get_settings().search_api_version)
    storage_resource_id: str = field(default_factory=lambda: get_settings().storage_resource_id)
    container_name: str = field(default_factory=lambda: get_settings().container_name)
    model_endpoint: str = field(default_factory=lambda: get_settings().model_endpoint.rstrip("/"))
    chat_deployment: str = field(default_factory=lambda: get_settings().chat_deployment)
    embedding_deployment: str = field(default_factory=lambda: get_settings().embedding_deployment)


class SearchClient:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        self._http = httpx.Client(base_url=self.settings.search_endpoint, timeout=120)

    def _headers(self) -> dict[str, str]:
        token = credential().get_token(SEARCH_SCOPE).token
        return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

    def request(self, method: str, path: str, body: Any | None = None) -> Any:
        resp = self._http.request(
            method,
            path,
            params={"api-version": self.settings.api_version},
            headers=self._headers(),
            json=body,
        )
        if resp.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {resp.status_code}: {resp.text}")
        return resp.json() if resp.content else None

    def get(self, path: str) -> Any:
        return self.request("GET", path)

    def put(self, path: str, body: Any) -> Any:
        return self.request("PUT", path, body)

    def post(self, path: str, body: Any) -> Any:
        return self.request("POST", path, body)

    def delete(self, path: str) -> Any:
        return self.request("DELETE", path)
