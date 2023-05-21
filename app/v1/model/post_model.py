# -*- coding: utf-8 -*-

from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from .base_model import CommonModel


class PostModel(CommonModel):
    __tablename__ = "posts"

    title = Column(String(30), nullable=False)
    description = Column(String(100), nullable=True)

    def __repr__(self):
        return f"<Post title={self.title}>"

    @validates("title")
    def validate_title(self, key, value):
        if not (value):
            raise ValueError("the title is required")

        if len(value) > 30:
            raise ValueError("the title no debe set mayor a 30")
        return value
