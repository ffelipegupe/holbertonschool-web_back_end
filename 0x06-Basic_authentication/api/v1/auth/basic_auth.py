#!/usr/bin/env python3
""" Basic Authorization
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class body
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Method that returns the Base64 part of the
            Authorization header for a Basic Authentication
        """
        if authorization_header is None or\
           type(authorization_header) is not str:
            return None
        head = authorization_header.split(' ')

        return head[1] if head[0] == 'Basic' else None
