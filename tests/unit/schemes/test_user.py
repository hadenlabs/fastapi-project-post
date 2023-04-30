# -*- coding: utf-8 -*-
import pytest
from faker import Faker
from faker.providers import internet, misc, profile
from hamcrest import assert_that, has_entries, not_none
from pydantic import ValidationError

from app.v1.schema import user_schema

fake = Faker()

fake.add_provider(misc)
fake.add_provider(profile)
fake.add_provider(internet)


test_user_success = [
    {
        "id": 1,
        "email": fake.email(),
        "username": fake.user_name(),
    },
    {
        "id": 2,
        "email": fake.email(),
        "username": fake.user_name(),
    },
]

test_user_create_success = [
    {
        "email": "myemail@infosisglobal.com",
        "username": "MyTypicalUsername",
        "password": "strongpass",
    },
    {
        "email": "myemail2@infosisglobal.com",
        "username": "MyTypicalUsername",
        "password": "123456789",
    },
]

test_user_create_failed = [
    {
        "username": "MyTypicalUsername",
        "password": "strongpass",
    },
    {
        "email": "myemail2@infosisglobal.com",
        "password": "123456789",
    },
]


@pytest.mark.parametrize("data", test_user_success)
def test_user_schema(data):
    user = user_schema.User(**data)
    assert_that(user, not_none())
    assert_that(user.dict(), has_entries(data), user)


@pytest.mark.parametrize("data", test_user_create_success)
def test_register_user_parametrize_success(data):
    user = user_schema.UserRegister(**data)
    assert_that(user, not_none())
    assert_that(user.dict(), has_entries(data), user)


@pytest.mark.parametrize("data", test_user_create_success)
def test_create_user_parametrize_success(data):
    user = user_schema.UserCreate(**data)
    assert_that(user, not_none())
    assert_that(user.dict(), has_entries(data), user)


@pytest.mark.parametrize("data", test_user_create_failed)
def test_register_user_parametrize_failed(data):
    with pytest.raises(ValidationError):
        user = user_schema.UserRegister(**data)
        assert_that(user, not_none())


@pytest.mark.parametrize("data", test_user_create_failed)
def test_create_user_parametrize_failed(data):
    with pytest.raises(ValidationError):
        user = user_schema.UserCreate(**data)
        assert_that(user, not_none())
