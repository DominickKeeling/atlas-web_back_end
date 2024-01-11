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

#!/usr/bin/env python3

""" Create a class LRUCache that inherits from BaseCaching
    and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Create a class LRUCache that inherits from BaseCaching
        and is a caching system """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.queue.remove(key)
        elif len(self.cache_data.keys()) >= self.MAX_ITEMS:
            discard = self.queue.pop(0)
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data.keys():
            return None
        self.queue.remove(key)
        self.queue.append(key)
        return self.cache_data[key]