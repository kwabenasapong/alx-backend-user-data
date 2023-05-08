#!/usr/bin/env python3

"""Module of SessionAuth"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        from uuid import uuid4
        if user_id is None or type(user_id) is not str:
            return None
        session_id = str(uuid4())
        SessionAuth().user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return user id based on session id
        """
        if session_id is None or type(session_id) is not str:
            return None
        return SessionAuth().user_id_by_session_id.get(session_id)
