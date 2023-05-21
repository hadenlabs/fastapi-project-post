# -*- coding: utf-8 -*-
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.v1.model.user_model import UserModel
from app.v1.schema import user_schema
from app.v1.service.auth_service import get_password_hash


def create_user(
    user: user_schema.UserRegister,
    db: Session,
) -> user_schema.User:
    get_user = (
        db.query(UserModel)
        .filter((UserModel.email == user.email) | (UserModel.username == user.username))
        .first()
    )

    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=msg)

    db_user = UserModel(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password),
    )

    db.add(db_user)
    db.commit()

    return user_schema.User(id=db_user.id, username=db_user.username, email=db_user.email)
