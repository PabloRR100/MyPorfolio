# project/api/config.py

from functools import lru_cache
import logging
from pathlib import Path
from pydantic import AnyUrl, BaseSettings, Field


logger = logging.getLogger("uvicorn")
env_file = Path(__file__).parent.parent / ".env"


class Settings(BaseSettings):
    class Config:
        env_file = env_file
        case_sensitive = True
        env_file_encoding = "utf-8"

    # API
    API_VERSION: str = Field(default="v1", env="API_VERSION")
    APP_PORT: int = Field(default=8000, env="APP_PORT")

    # POSTGRES
    DATABASE_URL: AnyUrl = Field(..., env="DATABASE_URL")
    DATABASE_URL_TEST: AnyUrl = Field(..., env="DATABASE_URL_TEST")

    # AUTH
    SECRET_KEY: str = Field(
        default="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7",
        env="SECRET_KEY",
    )
    ALGORITHM: str = Field(default="HS256", env="ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(
        default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES"
    )


@lru_cache
def get_settings() -> BaseSettings:
    """Function for loading global app settings. Can read from env vars or file.
    Settings are cached so that reading from a file (slow operation) is only called
    once.
    """
    print(f"Loading environmental variables from {env_file}.")
    return Settings()


if __name__ == "__main__":
    print("Settings: ", get_settings())
