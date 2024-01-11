#!/usr/bin/env python3

"""
Create a class LRUCache that inherits from BaseCaching and is a caching system:

You must use self.cache_data - dictionary from the parent class BaseCaching

You can overload def __init__(self): but dont forget to call the
parent init: super().__init__()

def put(self, key, item):
    Must assign to the dictionary self.cache_data the item value for the key key.
    If key or item is None, this method should not do anything.
    If the number of items in self.cache_data is higher
    than BaseCaching.MAX_ITEMS:
        you must discard the least recently used item (LRU algorithm)
        you must print DISCARD: with the key discarded and following by a new
        line

def get(self, key):
    Must return the value in self.cache_data linked to key.
    If key is None or if the key doesnt exist in self.cache_data, return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRU cache class """
    def __init__(self):
        """ Initializing """
        super.__init__()
        self.key_order = []

    def put(self, key, item):
        """ Appending item to the cache data """
        if key is not None and item is not None:
            if key in self.cach_data:
                self.key_order.remove(key)
            self.cache_data[key] = item
            self.key_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                lru_key = self.key_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}\n")

    def get(self, key):
        """ Retrieving key item, removing it and adding it again """
        if key is not None and key in self.cache_data:
            self.discarded_key.remove(key)
            self.discarded_key.append(key)
            return self.cache_data[key]
        return None