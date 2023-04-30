# -*- coding: utf-8 -*-
import pytest
from hamcrest import assert_that, not_none

from .factories import UserFactory

test_user_success = [
    {
        "email": "email@infosisglobal.com",
        "username": "username",
    },
    {
        "email": "email1@infosisglobal.com",
        "username": "username1",
    },
]


def test_make_user(db_setup):
    user = UserFactory()
    assert_that(user, not_none())


@pytest.mark.parametrize("data", test_user_success)
def test_make_user_parametrize(data, db_setup):
    user = UserFactory(**data)
    assert_that(user, not_none())
