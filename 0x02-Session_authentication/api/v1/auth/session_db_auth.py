#!/usr/bin/env python3

"""
SessionDBAuth module
"""

from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth Class"""
    def create_session(self, user_id=None):
        """Create and store new instance of UserSession
        and return Session id
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return User ID by requesting UserSession in the database
        based on session_id
        """
        if session_id is None or type(session_id) is not str:
            return None
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_session:
            return None
        if self.session_duration <= 0:
            return user_session[0].user_id
        if 'created_at' not in user_session[0].__dict__:
            return None
        created_at = user_session[0].__dict__.get('created_at')
        if created_at is None:
            return None
        if (created_at + timedelta(seconds=self.session_duration) <
                datetime.now()):
            return None
        return user_session[0].user_id

    def destroy_session(self, request=None):
        """Destroy the UserSession based on the Session ID
        from the request cookie
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        try:
            user_session = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not user_session:
            return False
        user_session[0].remove()
        return True
