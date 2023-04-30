# -*- coding: utf-8 -*-
import pytest
from fastapi import HTTPException
from hamcrest import assert_that, has_entries, not_none

from app.v1.schema import user_schema
from app.v1.service.user_service import create_user

test_user_success = [
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


def test_create_user_success(db_setup, db):
    data = {
        "email": "myemail@infosisglobal.com",
        "username": "MyTypicalUsername",
        "password": "strongpass",
    }
    user = user_schema.UserRegister(**data)
    del data["password"]
    response = create_user(user=user, db=db)
    assert_that(response, not_none())
    assert_that(response.dict(), has_entries(data))


@pytest.mark.parametrize("data", test_user_success)
def test_create_user_parametrize(data, db_setup, db):
    user = user_schema.UserRegister(**data)
    del data["password"]
    response = create_user(user=user, db=db)
    assert_that(response, not_none())
    assert_that(response.dict(), has_entries(data))


def test_user_duplicated(db_setup, db, user_factory):
    user = user_factory
    assert_that(user, not_none())

    data = {
        "username": user.username,
        "email": "myemail2@infosisglobal.com",
        "password": "123456789",
    }

    user_created = user_schema.UserRegister(**data)
    with pytest.raises(HTTPException):
        create_user(user=user_created, db=db)
