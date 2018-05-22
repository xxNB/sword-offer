
from collections import OrderedDict


class LruCache:
    def __init__(self, capacity=None):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache.keys():
            raise Exception("no this key")
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def put(self, key, value):
        # if len(self.cache) <= len(self.cache):
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) == self.capacity:
                # 弹出第一个
                self.cache.popitem(last=False)
                self.cache[key] = value
            else:
                self.cache[key] = value


cache = LruCache(capacity=2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)  # returns 1
cache.put(3, 3)  # 驱逐 key 2
# cache.get(2)  # raised
cache.put(4, 4)  # 驱逐 key 1
# cache.get(1)  # raised
# cache.get(3)  # returns 3
# cache.get(4)  # returns 4