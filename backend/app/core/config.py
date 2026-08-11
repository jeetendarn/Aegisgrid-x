from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    app_name: str = "AegisGrid X"
    app_env: str = "development"
    app_debug: bool = True

    backend_host: str = "127.0.0.1"
    backend_port: int = 8000

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "aegisgrid"
    database_user: str = "aegisgrid"
    database_password: str = ""

    redis_host: str = "localhost"
    redis_port: int = 6379

    kafka_bootstrap_servers: str = "localhost:9092"

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
