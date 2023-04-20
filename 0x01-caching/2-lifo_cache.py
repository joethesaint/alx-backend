#!/usr/bin/python3
""" 2. LIFO Caching
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ a class that inherits from BaseCaching and is
    a caching system.
    Arguments:
            key, item
    Methods:
            get(), post()
    """
    def __init__(self):
        """ initialize the class with the parent's init method
        """
        super().__init__()

    def put(self, key, item):
        """ assign to the dictionary self.cache_data the item value
        for the key"""
        if key or item is None:
            pass
        if len(self.cache_data) >= self.MAX_ITEMS:
            last_key = list(self.cache_data.keys())[-1]
            del self.cache_data[last_key]
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """
        Get the values associated with the key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
