#!/usr/bin/env python3

"""
Cache module
"""

import redis
import uuid
from typing import Union, Callable, Any
from functools import wraps


class Cache:
    """
    Cache class for storing and retrieving data from Redis.
    """

    def __init__(self):
        """
        Initialize a Cache object with a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]):
                The data to be stored in the cache.

        Returns:
            str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Callable[[bytes], Any] = None
    ) -> Union[str, bytes, int, float]:
        """
        Retrieve data from Redis using the provided key and
        apply the optional conversion function (fn).

        Args:
            key (str): The key used to retrieve data from Redis.
            fn (Callable[[bytes], Any], optional): A callable to
                convert the data to the desired format.

        Returns:
            Union[str, bytes, int, float]: The retrieved data,
                optionally converted using fn.
        """
        data = self._redis.get(key)
        if fn is not None and data is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve a string from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the string from Redis.

        Returns:
            str: The retrieved string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve an integer from Redis using the provided key.

        Args:
            key (str): The key used to retrieve the integer from Redis.

        Returns:
            int: The retrieved integer.
        """
        return self.get(key, fn=int)


def count_calls(fn: Callable) -> Callable:
    """
    A decorator to count how many times a method of the Cache class is called.
    """
    counts = {}  # To store call counts for different methods

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        method_name = fn.__qualname__
        if method_name in counts:
            counts[method_name] += 1
        else:
            counts[method_name] = 1

        result = fn(self, *args, **kwargs)
        return result

    return wrapper
