# -*- coding: utf-8 -*-
import os
from functools import lru_cache

from pydantic import BaseSettings

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Environment(BaseSettings):
    _db_name: str = os.getenv("DB_NAME")
    db_user: str = os.getenv("DB_USER")
    db_pass: str = os.getenv("DB_PASS")
    db_host: str = os.getenv("DB_HOST")
    db_port: str = os.getenv("DB_PORT", 5432)
    app_host: str = os.getenv("APPLICATION_HOST", "0.0.0.0")
    app_port: int = os.getenv("APPLICATION_PORT", 3000)

    secret_key: str = os.getenv("SECRET_KEY", "ed296226ec6de1cfe550fb2a979b6b71a80")
    token_expire: int = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 1440)

    @property
    def db_name(self):
        if os.getenv("ENVIRONMENT") == "testing":
            return "test_" + self._db_name

        return self._db_name

    @property
    def db_url(self):
        return (
            f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"
        )

    class Config:
        env_file = os.path.join(PROJECT_ROOT, ".env")


@lru_cache
def get_env() -> Environment:
    return Environment()
