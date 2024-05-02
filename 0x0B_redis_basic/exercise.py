#!/usr/bin/env python3

"""
Create a Cache class. In the __init__ method, store an instance of the Redis
    client as a private variable named _redis (using redis.Redis()) and flush
    the instance using flushdb.
Create a store method that takes a data argument and returns a string. The
    method should generate a random key (e.g. using uuid), store the input data
    in Redis using the random key and return the key.
Type-annotate store correctly. Remember that data can be a str, bytes, int or
float.
"""

from typing import Union, Callable, Optional
import uuid
import redis
import functools


def count_calls(method: Callable) -> Callable:
    """ defines a method calllable and returns a Callable """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Increments the count using Redis INCR """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    # method might be refering to the get_method func. so might need to chng to that    
    return wrapper

def call_history(method: Callable) -> Callable:
    """ stores the history of inputs and outputs """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        
        self._redis.rpush(input_key, str(args))
        
        result = method(self, *args, **kwargs)
        
        self._redis.rpush(output_key, str(result))
        
        return result
    return wrapper

        
class Cache:
    def __init__(self):
        """
        Initializing the cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Accepts data types and returns a str """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key

    def get_method(self, key: str, fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]] = None) -> Union[str, int, float, None]:
        """ defines get with a key argument and an optional fn arg if callable"""
        value = self._redis.get(key)
        if value is not None and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """ fetches strings and ints from redis by predefining the conv functions"""
        return self.get_method(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get_method(key, lambda x: x. int(x))

def replay(cache_instance: Cache, method_name: str):
    """ replays the history of calls to a specific method """
    input_key =  f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = cache_instance._redis.lrange(input_key, 0, -1)
    outputs = cache_instance._redis.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")

    for index, (input_item, output_item) in enumerate(zip(inputs, outputs), start=1):

        input_decoded = input_item.decode('utf-8')
        output_decoded = output_item.decode('utf-8')

        print(f"{index}. {method_name}(*{input_decoded}) -> {output_decoded}")
