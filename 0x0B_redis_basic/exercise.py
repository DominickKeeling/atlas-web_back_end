#!/usr/bin/env python3

"""
Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

Type-annotate store correctly. Remember that data can be a str, bytes, int or float.
"""
import functools
import redis
import uuid
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    count the methods called in the class
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        intercepts calls to the original method and adds counting functionality
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    stores the history of the inputs and the outputs for each function call
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        intercepts calls to original method and adds history log functionality
        """
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"
        
        self._redis.rpush(input_key, *[str(args) for arg in args])
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


class Cache():
    """
    this is the cache class
    """
    def __init__(self):
        """
        initializing the cache class
        """
        self._redis = redis.Redis(host='localhost', port=6379)
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        defining the store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int]:
        """
        retrieves key from redis
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Union[str, bytes, int]:
        """
        this method decodes the string from bytes
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: int) -> Union[str, bytes, int]:
        """
        retrieves value from redis and converts to int
        """
        return self.get(key, fn=int)

    def replay(func):
        """
        function that displays the history of calls of a particular function
        """
        function_name = func.__qualname__
        input_key = function_name + ":inputs"
        output_key = function_name + ":outputs"

        inputs = redis_client.lrange(input_key, 0, -1)
        outputs = redis_client.lrange(output_key, 0, -1)
        print(f"{function_name} was called {len(inputs)} times:")

        for input_data, output_data in zip(inputs, outputs)
            input_data = input_data.decode("utf-8") if isinstance(input_data, bytes) else input_data
            output_data = output_data.decode("utf-8") if isinstance(output_data, bytes) else output_data

        print(f"{function_name}(*({input_data},)) -> {output_data}")
