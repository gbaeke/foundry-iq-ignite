from functools import lru_cache
from typing import Any

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Every setting the app reads, from the environment or .env. .env.example lists them all (a test checks)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    host: str = "127.0.0.1"
    port: int = 8318  # local default, derived from the app's name
    log_json: bool = False  # JSON log lines

    # Azure resources (written by infra/deploy.sh and the plugin connect step)
    azure_subscription_id: str = ""
    resource_group: str = ""
    search_endpoint: str = ""  # the Foundry IQ (Azure AI Search) service, West US 3
    search_api_version: str = "2026-11-01-preview"
    storage_account: str = ""
    storage_resource_id: str = ""
    container_name: str = "kestrel-corpus"
    model_endpoint: str = ""  # Azure OpenAI / Foundry resource with the chat and embedding deployments
    chat_deployment: str = "gpt-5.6-luna"
    embedding_deployment: str = "text-embedding-3-small"


@lru_cache
def get_settings() -> Settings:
    return Settings()


def settings_without_env_file(**values: Any) -> Settings:
    """Settings from these values and the environment only: .env is not read (tests, tools)."""
    return Settings(_env_file=None, **values)  # pyright: ignore[reportCallIssue]  (pydantic-settings' init option)
