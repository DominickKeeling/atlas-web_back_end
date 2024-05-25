#!/usr/bin/env python3

"""
Create a class MRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching
You can overload def __init__(self): but don’t forget to call the parent init:
super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the item value for the key key.
If key or item is None, this method should not do anything.
If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
you must discard the most recently used item (MRU algorithm)
you must print DISCARD: with the key discarded and following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in self.cache_data, return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching system
    """
    def __init__(self):
        """ initializing the class """
        super().__init__()

    def put(self, key, item):
        """ appending item to cache data """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.access_order.remove(key)
        self.access_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = next(reversed(self.cache_data))
            print(f"DISCARD: {mru_key}\n")
            del self.cache_data[mru_key]
        self.cache_data[key] = item

    def get(self, key):
        """ returns value by key """
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
