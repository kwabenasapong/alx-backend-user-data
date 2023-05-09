#!/usr/bin/env python3

"""
Create a new model UserSession in models/user_session.py that inherits from Base:

Implement the def __init__(self, *args: list, **kwargs: dict): like in User but for these 2 attributes:
user_id: string
session_id: string
"""

from models.base import Base


class UserSession(Base):
    """UserSession Class"""
    def __init__(self, *args: list, **kwargs: dict):
        """Constructor"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
