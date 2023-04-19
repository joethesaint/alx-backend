#!/usr/bin/env python3
""" 0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ a class that inherits from BaseCaching and is
        a caching system.
        Attributes:
            key, item
        Methods:
            put(), get()
    """

    def _init_(self):
        super()._init_()
        self.cache_data = {}

    def put(self, key, item):
        """ Assign key and item to the cache system """
        if key is None or item is None:
            pass
        self.cache_data[key] = item

    def get(self, key):
        """ Get the value from the cache with key"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
