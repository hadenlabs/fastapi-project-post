# -*- coding: utf-8 -*-
import os
from functools import lru_cache

from decouple import config
from pydantic import BaseSettings

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Environment(BaseSettings):
    _db_name: str = config("DB_NAME")
    debug: bool = config("DEBUG", default=False, cast=bool)
    db_user: str = config("DB_USER")
    db_pass: str = config("DB_PASS")
    db_host: str = config("DB_HOST", default="127.0.0.1")
    db_port: int = config("DB_PORT", default=5432, cast=int)
    app_host: str = config("APPLICATION_HOST", default="0.0.0.0")
    app_port: int = config("APPLICATION_PORT", default=8000, cast=int)
    secret_key: str = config("SECRET_KEY", default="ed296226ec6de1cfe550fb2a979b6b71a80")
    token_expire: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", default=1440, cast=int)

    @property
    def db_name(self):
        if os.getenv("STAGE") == "testing":
            return "test_" + self._db_name

        return self._db_name

    @property
    def db_url(self):
        return f"postgresql://{self.db_user}:{self.db_pass}@{self.db_host}/{self.db_name}"

    class Config:
        env_file = os.path.join(PROJECT_ROOT, ".env")


@lru_cache
def get_env() -> Environment:
    return Environment()
