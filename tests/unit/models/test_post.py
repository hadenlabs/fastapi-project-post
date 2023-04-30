# -*- coding: utf-8 -*-
import pytest
from hamcrest import assert_that, equal_to, not_none

from app.v1.model.post_model import PostModel

data_post_register_success = [
    {"title": "hey man", "description": "test test"},
    {"title": "hey man", "description": ""},
]

data_post_register_failed = [
    {"title": "hey man ddddddddddddddddddddddd", "description": "test test"},
    {"title": "", "description": "test test"},
]


def test_model_post_success():
    post = PostModel()
    assert_that(post, not_none())
    assert_that(post.__tablename__, equal_to("posts"))


@pytest.mark.parametrize("data", data_post_register_success)
def test_post_register_success(data):
    post = PostModel(**data)
    assert_that(post, not_none())


@pytest.mark.parametrize("data", data_post_register_failed)
def test_post_register_failed(data):
    with pytest.raises(ValueError):
        post = PostModel(**data)
        assert_that(post, not_none())
