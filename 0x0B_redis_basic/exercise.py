#!/usr/bin/env python3

import redis
import uuid
import functools
from typing import Union, Optional, Callable


def count_calls(method: Callable) -> Callable:

  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    
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
  def __init__(self):
    self._redis = redis.Redis()
    self._redis.flushdb()

  @count_calls
  @call_history 
  def store(self, data: Union[str, bytes, int, float]) -> str:
    key = str(uuid.uuid4())
    self._redis.set(key, data)
    return key

  def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, None]:
    data = self._redis.get(key)
    
    if data is None:
      return None
    
    if fn is not None:
      return fn(data)
    
    return data
    
  def get_str(self, key: str) -> str:
    return self.get(key, fn=lambda d: d.decode("utf-8"))

  def get_int(self, key: str) -> int:
    return self.get(key, fn=int)
  
def replay(method: callable):
  """ replays the call history of a method """
  redis_instance = method.__self__._redis
  method = method.__qualname__
  
  input_key = method.__qualname__ + ":inputs"
  output_key = method.__qualname__ + ":outputs"
  
  inputs = redis_instance.lrange(input_key, 0, -1)
  outputs = redis_instance.lrange(output_key, 0, -1)
  
  call_count = len(inputs)
  
  print(f"{method_name} was called {call_count} times:")
  
  for input_args, output in zip(inputs, outputs):
    decoded_input = input_args.decode('utf-8')
    decoded_output = output.decode('utf-8')
    print(f"{method_name}(*{decoded_input}) -> {decoded_output}")