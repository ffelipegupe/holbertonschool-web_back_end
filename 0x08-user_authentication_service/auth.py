#!/usr/bin/env python3
""" Authorization module
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    """ Method that takes in a password string arguments and returns bytes.
        The returned bytes is a salted hash of the input password,
        hashed with bcrypt.hashpw.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Function that returns a string representation of a new UUID """
    return str(uuid4())


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

    def create_session(self, email: str) -> str:
        """ Method that finds the user corresponding to the email,
            generates a new UUID and store it in the database as the
            user’s session_id
        """
        try:
            src = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(src.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """ Method that gets a user from its session_id """
        if not session_id:
            return None
        try:
            src = self._db.find_user_by(session_id=session_id)
            return src
        except NoResultFound:
            None

    def destroy_session(self, user_id: str) -> None:
        """ Method updates the corresponding user’s session ID to None
        """
        try:
            self._db.update_user(user_id=user_id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """ Method that returns a token """
        try:
            src = self._db.find_user_by(email=email)
            tkn = _generate_uuid()
            self._db.update_user(src.id, reset_token=tkn)
            return tkn
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Method that updates user's password """
        try:
            src = self._db.find_user_by(reset_token=reset_token)
            psw = _hash_password(password)
            self.db.update_user(src.id, hashed_password=psw, reset_token=None)
        except NoResultFound:
            raise ValueError
