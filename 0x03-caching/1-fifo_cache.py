#!/usr/bin/python3
""" FIFO caching module """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching
        and is a caching system """
    def __init__(self):
        """ Initialize class instance. """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add key/value pair to cache data."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """Return value stored in `key` key of cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
