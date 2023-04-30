# -*- coding: utf-8 -*-
import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database

from app.core.config import Environment, get_env
from app.core.db.session import Base, engine
from testing.validation import assert_test_database
from tests.db.session import session


def create_test_database(settings: Environment):
    assert_test_database(settings=settings)
    if database_exists(settings.db_url):
        drop_database(settings.db_url)
    create_database(settings.db_url)
    Base.metadata.create_all(bind=engine)


@pytest.fixture
def db(settings: Environment):
    try:
        db = session
        yield db
    finally:
        db.close()


@pytest.fixture
def db_setup(settings: Environment):
    create_test_database(settings=get_env())


def pytest_sessionfinish(session, exitstatus):
    if database_exists(get_env().db_url):
        drop_database(get_env().db_url)
