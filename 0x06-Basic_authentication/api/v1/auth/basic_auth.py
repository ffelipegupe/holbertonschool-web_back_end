#!/usr/bin/env python3
""" Basic Authorization
"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Method that returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or\
           type(base64_authorization_header) is not str:
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            message_bytes = base64.b64decode(base64_bytes)
            message = message_bytes.decode('utf-8')
            return message
        except Exception:
            return None
