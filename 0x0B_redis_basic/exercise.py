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


def call_history(method: Callable) -> Callable:
    """ Method that stores the history of inputs and outputs """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """ Wrapper function """
        self._redis.rpush(inputs, str(args))
        res = method(self, *args)
        self._redis.rpush(outputs, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """ Method that displays the history of calls of a particular function
    """
    inst = redis.Redis()
    storage = method.__qualname__
    aux = inst.get(storage).decode('utf-8')
    inputs = inst.lrange(storage + ':inputs', 0, -1)
    outputs = inst.lrange(storage + ':outputs', 0, -1)
    print("{} was called {} times:".format(storage, aux))
    for inp, out in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(storage, inp.decode("utf-8"),
                                     out.decode("utf-8")))


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
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
