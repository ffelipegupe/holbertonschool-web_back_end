#!/usr/bin/env python3
""" Basic Authorization
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class body
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ Returns the user email and password from the Base64 decoded value
        """
        if not decoded_base64_authorization_header or\
           not isinstance(decoded_base64_authorization_header, str)\
           or ":" not in decoded_base64_authorization_header:
            return (None, None)
        extract = decoded_base64_authorization_header.split(':', 1)
        return (extract[0], extract[1]) if extract else (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """ Method that returns the User instance
            based on his email and password
        """
        if user_email is None or type(user_email) is not str or \
           user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except KeyError:
            return None

        if len(users) == 0:
            return None

        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that overloads Auth and
            retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            base64_h = self.extract_base64_authorization_header(header)
            decode_h = self.decode_base64_authorization_header(base64_h)
            credents = self.extract_user_credentials(decode_h)
            return self.user_object_from_credentials(credents[0], credents[1])
        except Exception:
            return None
