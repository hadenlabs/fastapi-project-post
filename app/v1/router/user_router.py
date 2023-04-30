# -*- coding: utf-8 -*-
from fastapi import APIRouter, Body, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core import deps
from app.v1.schema import user_schema
from app.v1.schema.token_schema import Token
from app.v1.service import auth_service, user_service

router = APIRouter(prefix="/api/v1", tags=["users"])


@router.post(
    "/user/",
    status_code=status.HTTP_201_CREATED,
    response_model=user_schema.User,
    summary="Create a new user",
)
def create_user(
    user: user_schema.UserRegister = Body(...), db: Session = Depends(deps.get_db)
):
    """
    ## Create a new user in the app

    ### Args
    The app can receive next fields into a JSON
    - email: A valid email
    - username: Unique username
    - password: Strong password for authentication

    ### Returns
    - user: User info
    """
    return user_service.create_user(user=user, db=db)


@router.post("/login", tags=["users"], response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(deps.get_db)
):
    """
    ## Login for access token

    ### Args
    The app can receive next fields by form data
    - username: Your username or email
    - password: Your password

    ### Returns
    - access token and token type
    """
    access_token = auth_service.generate_token(
        db=db, username=form_data.username, password=form_data.password
    )
    return Token(access_token=access_token, token_type="bearer")
