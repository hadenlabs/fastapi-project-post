# -*- coding: utf-8 -*-
from typing import Generator

from app.core.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
