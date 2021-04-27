#!/usr/bin/env python3
""" Redis basci Module """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that generates a random key,
            stores the input data in Redis using the random key
            and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key