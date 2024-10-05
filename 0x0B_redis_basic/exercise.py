#!/usr/bin/env python3

import redis
import uuid
import functools
from typing import Union, Optional, Callable

class Cache:
  def __init__(self):
    self._redis = redis.Redis()
    self._redis.flushdb()

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


def count_calls(method: Callable) -> Callable:

  @functools.wraps(method)
  def wrapper(self, *args, **kwargs):
    
    key = method.__qualname__
    
    self._redis.incr(key)
    
    return method(self, *args, **kwargs)

  return wrapper