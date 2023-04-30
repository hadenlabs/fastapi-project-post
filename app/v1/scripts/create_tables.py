# -*- coding: utf-8 -*-
from app.core.db.session import Base, engine


def create_tables():
    Base.metadata.create_all(engine)
