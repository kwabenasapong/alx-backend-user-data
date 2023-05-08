#!/usr/bin/env python3
""" Auth module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require_auth method
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        ''' allowing * at the end of excluded paths'''
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '*':
                if path.startswith(excluded_path[:-1]):
                    return False
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None

    def session_cookie(self, request=None):
        """Return cookie value from request
        """
        from os import getenv
        if request is None:
            return None
        return request.cookies.get(getenv('SESSION_NAME'))
