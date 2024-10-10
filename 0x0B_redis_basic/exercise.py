#!/usr/bin/env python3

import redis
import uuid
import functools
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:
  """ tracks how many times a method is called"""

  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    # Increment the call count in Redis using the method's qualified name
    key = method.__qualname__
    
    self._redis.incr(key)
    
    return method(self, *args, **kwargs)

  return wrapper


def call_history(method: Callable) -> Callable:
  """ increments the call count of a  method """
  
  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    # creates redis keys for inputs and outputs
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"
    
    self._redis.rpush(input_key, str(args))
    
    output = method(self, *args, **kwargs)
    
    self._redis.rpush(output_key, str(output))
    return output
  return wrapper

class Cache:
  """ A class that provides a cache interface using Redis for storing, retrieving, and tracking data."""
  def __init__(self):
    """Initializes the Cache by setting up a connection to Redis and flushing the Redis database."""
    self._redis = redis.Redis()
    self._redis.flushdb()

  @count_calls
  @call_history 
  def store(self, data: Union[str, bytes, int, float]) -> str:
    """Stores data in Redis and returns the generated UUID key."""
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key

  def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
    """ Retrieves data from Redis using the provided key."""
    data = self._redis.get(key)
    
    if data is None:
      return None
    
    if fn is not None:
      return fn(data)
    
    return data
    
  def get_str(self, key: str) -> str:
    """ Retrieves a string from Redis by its key, ensuring the data is decoded from bytes to a string."""
    return self.get(key, fn=lambda d: d.decode("utf-8"))

  def get_int(self, key: str) -> int:
    """ Retrieves an integer from Redis by its key."""
    return self.get(key, fn=int)
  
def replay(method: callable):
  """ replays the call history of a method """
  redis_instance = method.__self__._redis
  
  method_name = method.__qualname__
  
  input_key = f"{method_name}:inputs"
  output_key = f"{method_name}:outputs"
  
  inputs = redis_instance.lrange(input_key, 0, -1)
  outputs = redis_instance.lrange(output_key, 0, -1)
  
  call_count = len(inputs)
  
  print(f"{method_name} was called {call_count} times:")
  
  for input_args, output in zip(inputs, outputs):
    decoded_input = input_args.decode('utf-8')
    decoded_output = output.decode('utf-8')
    print(f"{method_name}(*{decoded_input}) -> {decoded_output}")