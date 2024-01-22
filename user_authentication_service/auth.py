#!/usr/bin/env python3

""" In this task you will define a _hash_password method that takes in a
password string arguments and returns bytes.
The returned bytes is a salted hash of the input password, hashed with
bcrypt.hashpw."""

from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """ Takes in a password string arguments and returns bytes"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def _generate_uuid() -> str:
    """ Returns a string representation of new UUID."""
    string_uuid = str(uuid.uuid4())
    return string_uuid


class Auth:
    """interacts with the authentication database."""

    def __init__(self):
        """ Instance of the Auth class """
        self._db = DB()

    def register_user(self, email: str,
                      password: str) -> User:
        '''Returns user object after creating
        user'''
        try:
            already_exist = self._db.find_user_by(email=email)
            if already_exist:
                raise ValueError('User {} already exists'.format(email))

        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """if mail and pwd match returns true"""
        try:
            user = self._db.find_user_by(email=email)
            if not user:
                return False

            if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
                return True

        except NoResultFound:
            pass

        return False

    def create_session(self, email: str) -> str:
        """Returns the session id"""
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Returns the users email"""
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user.email
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Updates user session id """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        except NoResultFound:
            return None
          