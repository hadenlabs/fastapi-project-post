# -*- coding: utf-8 -*-
import pytest
from email_validator import EmailNotValidError
from hamcrest import assert_that, equal_to, not_none

from app.v1.model.user_model import UserModel

data_user_success = [
    {
        "email": "email@gmail.com",
        "username": "user1",
        "password": "123456789",
    },
    {
        "email": "email@gmail.com",
        "username": "user1",
        "password": "123456789",
    },
]

data_user_failed = [
    {
        "email": "email",
        "username": "user1",
        "password": "123456789",
    },
    {
        "email": "email@gmail.com",
        "username": "user1",
        "password": "1289",
    },
]

data_user_email_failed = [
    {
        "email": "email",
        "username": "user1",
        "password": "123456789",
    },
    {
        "email": "email@",
        "username": "user1",
        "password": "123456789",
    },
    {
        "email": "email@com",
        "username": "user1",
        "password": "123456789",
    },
]


@pytest.mark.parametrize("data", data_user_success)
def test_user_model_success(data):
    user = UserModel(**data)
    assert_that(user, not_none())
    assert_that(user.__tablename__, equal_to("users"))


@pytest.mark.parametrize("data", data_user_failed)
def test_user_validate_failed(data):
    with pytest.raises(ValueError):
        user = UserModel(**data)
        assert_that(user, not_none())


@pytest.mark.parametrize("data", data_user_email_failed)
def test_email_validate_failed(data):
    with pytest.raises(EmailNotValidError):
        user = UserModel(**data)
        assert_that(user, not_none())
