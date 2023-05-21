# -*- coding: utf-8 -*-
from typing import List, Optional

from pydantic import EmailStr, Field

from .base_schema import CommonBase


class UserBase(CommonBase):
    email: EmailStr = Field(..., example="myemail@infosisglobal.com")
    username: str = Field(..., min_length=3, max_length=100, example="MyTypicalUsername")


class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=100, example="strongpass")


class UserRegister(UserCreate):
    pass


class User(UserBase):
    id: int = Field(..., example="5")

    class Config:
        orm_mode = True
