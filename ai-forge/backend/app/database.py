from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Forge"
    app_env: str = "development"
    app_debug: bool = True
    app_port: int = 8000
    secret_key: str = "change-me-in-production"
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/ai_forge"
    nvidia_api_key: str = ""
    nvidia_base_url: str = "https://integrate.api.nvidia.com/v1"
    openrouter_api_key: str = ""
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    local_nim_base_url: str = "http://localhost:8000/v1"
    github_app_id: str = ""
    github_app_private_key_path: str = "/run/secrets/github_app_private_key"
    github_webhook_secret: str = ""
    github_client_id: str = ""
    github_client_secret: str = ""
    workspace_root: str = "/workspaces"
    allowed_repo_hosts: str = "github.com"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
