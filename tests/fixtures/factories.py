# -*- coding: utf-8 -*-
import pytest
from hamcrest import assert_that, not_none

from app.v1.schema import user_schema
from app.v1.service.user_service import create_user


@pytest.fixture()
def user_factory(db) -> user_schema.User:
    data = {
        "email": "emailrepetido@infosisglobal.com",
        "username": "MyTypicalUsername",
        "password": "strongpass",
    }
    user = user_schema.UserRegister(**data)
    response = create_user(user=user, db=db)
    assert_that(response, not_none())
    return response
