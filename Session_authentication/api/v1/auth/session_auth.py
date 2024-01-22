#!/usr/bin/env python3

""" Session auth class """

import uuid
from models.user import User
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Class for user sessions """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ creates a  session ID for user """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())

        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """finds and returns user_id ascociated with the given session_id """
        if session_id is None or not isinstance(session_id, str):
            return None

        user_id = self.user_id_by_session_id.get(session_id)

        return user_id

    def current_user(self, request=None):
        """ method that returns a user instance based on cookie value """

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """ deletes the user session/logout """

        if request is None:
            return False

        session_id_cookie = self.session_cookie(request)
        if session_id_cookie is None:
            return False

        user_id = self.user_id_for_session_id(session_id_cookie)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id_cookie]
        return True
