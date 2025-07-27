import pathlib

from pydantic import BaseSettings
from typing import Optional

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    AUTH_PREFIX: str = "/auth"
    TOKEN_ENDPOINT: str = "/token"
    JWT_SECRET: str = "DEVELOPMENT-CINEMA-SECRET-TOKEN"
    ALGORITHM: str = "HS256"
    STATIC_STORAGE_DIR: str = f"{ROOT}/static"
    STATIC_API_PATH: str = "/static"

    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///cinema.db"

    class Config:
        case_sensitive = True


settings = Settings()
