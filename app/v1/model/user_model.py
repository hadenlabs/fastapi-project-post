# -*- coding: utf-8 -*-

from email_validator import EmailNotValidError, validate_email
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, validates

from .base_model import CommonModel


class UserModel(CommonModel):
    __tablename__ = "users"
    email = Column(String(100), nullable=False, unique=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User email={self.email}>"

    @validates("email")
    def validate_email(self, key, value):
        if not validate_email(value):
            raise EmailNotValidError("failed validation email")
        return value

    @validates("password")
    def validate_password(self, key, value):
        if len(value) <= 8:
            raise ValueError("failed password >= 8")
        return value
