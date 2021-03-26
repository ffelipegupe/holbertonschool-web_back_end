#!/usr/bin/python3
""" LIFOCache module. """

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Class LIFOCache that inherits from BaseCaching
        and is a caching system """
    def __init__(self):
        """ Initialization """
        super().__init__()

    def put(self, key, item):
        """ Adds an item in the cache. """
        if not (key is None or item is None):
            if (
                len(self.cache_data.keys()) == BaseCaching.MAX_ITEMS and
                (key not in self.cache_data.keys())
            ):
                last = sorted(self.cache_data.keys())[-1]
                print('DISCARD: {}'.format(last))
                del self.cache_data[last]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Gets an item by key. """
        if key not in self.cache_data.keys():
            return None
        else:
            return self.cache_data[key]
