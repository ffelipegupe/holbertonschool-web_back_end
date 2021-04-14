#!/usr/bin/env python3
""" Authorization module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """ method that takes in a password string arguments and returns bytes.
            The returned bytes is a salted hash of the input password,
            hashed with bcrypt.hashpw.
        """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Auth Constructor """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method to register an User """
        try:
            if self._db.find_user_by(email=email):
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Method to validate logins """
        try:
            src = self._db.find_user_by(email=email)
            return bcrypt.checkpw(str.encode(password), src.hashed_password)
        except NoResultFound:
            return False
