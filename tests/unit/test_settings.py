# -*- coding: utf-8 -*-
import os

from hamcrest import assert_that
from mock import patch

from app.core.config import Environment, get_env


@patch.dict(os.environ, {"STAGE": "testing"})
def test_configuration_environment_test():
    settings: Environment = get_env()
    assert_that(settings.db_name.startswith("test"), True, settings.db_name)
