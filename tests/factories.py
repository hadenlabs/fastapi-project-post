# -*- coding: utf-8 -*-
import factory

from app.v1.model.user_model import UserModel

from .db.session import session


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserModel
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    email = factory.Sequence(lambda n: f"username{n}@email.com")
    username = factory.Sequence(lambda n: f"username{n}")
    password = factory.Sequence(lambda n: f"username{n}")
