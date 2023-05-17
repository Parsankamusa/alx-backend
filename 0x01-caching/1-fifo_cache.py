#!/usr/bin/python3
''' FIFO caching: Create a class FIFOCache that inherits from BaseCaching
                  and is a caching system
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' A FIFO Cache.
        Inherits all behaviors from BaseCaching except, upon any attempt to
        add an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the oldest entry to accommodate for
        the new one.
        Attributes:
          __init__ - method that initializes class instance
          put - method that adds a key/value pair to cache
          get - method that retrieves a key/value pair from cache '''
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the first item put in cache (FIFO algorithm)
                oldest_key = next(iter(self.cache_data))
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}\n")

            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None

