#!/usr/bin/env python3

"""Module for Session Expiration"""

from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""
    def __init__(self):
        """Constructor"""
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            self.session_duration = 0
    
    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        SessionAuth.user_id_by_session_id[session_id] = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Gets user_id from session_id"""
        if session_id is None:
            return None
        session_dictionary = SessionAuth.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get('user_id')
        if 'created_at' not in session_dictionary:
            return None
        created_at = session_dictionary.get('created_at')
        if created_at is None:
            return None
        if (created_at + timedelta(seconds=self.session_duration) <
                datetime.now()):
            return None
        return session_dictionary.get('user_id')
