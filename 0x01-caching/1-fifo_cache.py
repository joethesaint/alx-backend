#!/usr/bin/python3
""" 1. FIFO caching
"""
from collections import deque

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache (BaseCaching):
    """ a class that inherits from BaseCaching and is a caching system
        Methods:
                put: to change the elements
                get: assign a key to the value
    """
    def __init__(self):
        """ init function
        """
        super().__init__()
        self.lineup = []

    def put(self, key, item):
        """ assign to the dictionary self.cache_data, the time value
        for the key
        """
        # if key or item is none, method should not do anything
        if key or item is None:
            pass
        # if the number of item in self.cache_data is higher
        # than BaseCaching.MAX_ITEMS:
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # can be also self.MAX_ITEMS
            # discard the first item put in cache (FIFO algorithm)
            to_discard = self.lineup[0]
            del self.cache_data[to_discard]
            self.lineup.pop(0)
            # print DISCARD: with the key discarded, followed by new line
            print(f"DISCARD: {to_discard}")
        self.lineup.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ assign key to a value
        key to be present in cache_data
        """
        # if key is None or if key doesn't exist in self.cache_data :-> None
        if key is None and key not in self.cache_data:
            return None
        # return the value in self.cache_data linked to key
        else:
            return self.cache_data[key]
