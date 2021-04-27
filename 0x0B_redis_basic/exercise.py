#!/usr/bin/env python3
""" Redis basci Module """
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Method that increments the count for that key every time the method
        is called and returns the value returned by the original method.
    """
    method_ = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        """ Wrapper function """
        c = method(self, args)
        self._redis.incr(method_)
        return c
    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
