#!/usr/bin/python3
""" Basic dictionary """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Class BasicCache that inherits from BaseCaching and is a caching system """

    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
