from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AegisGrid X"
    app_env: str = "development"
    app_debug: bool = True

    backend_host: str = "127.0.0.1"
    backend_port: int = 8000

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
