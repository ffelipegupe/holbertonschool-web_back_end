#!/usr/bin/env python3
""" API authentication 
"""
from flask import request
from typing import List, TypeVar


class Auth():
    """ class to manage the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ require auth method
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != '/':
            path += '/'
        for p in excluded_paths:
            if p.endswith('*'):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """ authorization header method
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        return None
