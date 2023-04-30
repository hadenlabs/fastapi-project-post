# -*- coding: utf-8 -*-
from fastapi import status
from hamcrest import assert_that, equal_to, not_none


def test_create_user_ok(db_setup, test_client):
    client = test_client

    user = {
        "email": "test_create_user_ok@infosisglobal.com",
        "username": "test_create_user_ok",
        "password": "admin12345",
    }

    response = client.post(
        "/api/v1/user/",
        json=user,
    )
    assert_that(response.status_code, equal_to(status.HTTP_201_CREATED), response.text)
    data = response.json()
    assert_that(data["email"], equal_to(user["email"]))
    assert_that(data["username"], equal_to(user["username"]))


def test_create_user_duplicate_email(db_setup, user_factory, test_client):
    client = test_client
    user = user_factory
    assert_that(user, not_none())

    data = {
        "email": user.email,
        "username": "test_create_user_duplicate_email",
        "password": "admin12345",
    }

    response = client.post(
        "/api/v1/user/",
        json=data,
    )
    assert_that(
        response.status_code, equal_to(status.HTTP_400_BAD_REQUEST), response.text
    )
    data = response.json()
    assert_that(data["detail"], equal_to("Email already registered"))


def test_create_user_duplicate_username(db_setup, user_factory, test_client):
    client = test_client
    user = user_factory
    assert_that(user, not_none())

    data = {
        "email": "test_create_user_duplicate_username@infosisglobal.com",
        "username": user.username,
        "password": "admin12345",
    }

    response = client.post(
        "/api/v1/user/",
        json=data,
    )
    assert_that(
        response.status_code, equal_to(status.HTTP_400_BAD_REQUEST), response.text
    )
    data = response.json()
    assert_that(data["detail"], equal_to("Username already registered"))
