# -*- coding: utf-8 -*-

from sqlalchemy.orm import scoped_session

from app.core.db.session import SessionLocal

session: scoped_session = scoped_session(SessionLocal)
