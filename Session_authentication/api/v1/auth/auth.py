#!/usr/bin/env python3

""" Create a class to manage the API auth """

from flask import request
from typing import List, TypeVar
import os


class Auth():
    """ auth class """

    def __init__(self):
        """ init """
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ define authorization_header """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self) -> TypeVar('User'):
        """ define current_user """
        return None

    def session_cookie(self, request=None):
        """ returns the value of the session cookie """

        if request is None:
            return None

        session_name = os.getenv('SESSION_NAME', '_my_session_id')

        cookie_value = request.cookies.get(session_name)

        return cookie_value
