# -*- coding: utf-8 -*-
import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def test_client() -> TestClient:
    """Return client test"""
    client = TestClient(app)
    return client


@pytest.fixture
def access_token(test_client: TestClient) -> str:
    """Return access token"""
    client = test_client
    username = "elliot"
    password = "admin12345"

    user = {
        "email": f"{username}@infosisglobal.com",
        "username": username,
        "password": password,
    }

    response = client.post(
        "/api/v1/user/",
        json=user,
    )

    login = {"username": username, "password": password}

    response = client.post(
        "/api/v1/login/",
        data=login,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        allow_redirects=True,
    )

    data = response.json()

    return data["access_token"]
