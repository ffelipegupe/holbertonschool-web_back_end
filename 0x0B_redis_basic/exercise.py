#!/usr/bin/env python3
""" Redis basci Module """
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """ Method that converts data to a desired format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """ Method that converts data to string format
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """ Method that converts data to int
        """
        return self.get(key, int)
