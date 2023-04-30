# -*- coding: utf-8 -*-
import pytest

from app.core.config import get_env


@pytest.fixture
def settings():
    """Return settings"""
    return get_env()
