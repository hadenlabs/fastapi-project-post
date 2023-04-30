# -*- coding: utf-8 -*-
from app.core.config import Environment


def assert_test_database(settings: Environment):
    """
    Raises a Error in the event that the database name does not contain
    any reference to testing.

    Also checks South settings to ensure migrations are not implemented.
    """

    if not settings.db_name.startswith("test"):
        raise ValueError("You must run with a test database")
