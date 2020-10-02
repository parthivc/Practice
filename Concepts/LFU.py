# A Least Frequently Used Cache implementation in Python3
# All operations are in O(1) and O(log(n)) time for different implementations


# This is the log(n) implementation

class easyLFUNode:
    def __init__(self, a=None, b=None):
        self.key = a
        self.value = b

    def assign(self, key, value):
        self.key = key
        self.value = value


class easyLFU:
    def __init__(self, size):
        self.capacity = size
        self.size = 0
        self.cache = [None] * size
        self.indices = dict()

    def parent(self, value):
        return value >> 1

    def left(self, value):
        return value << 1

    def right(self, value):
        return (value << 1) + 1

    def insert(self, key, value):
        if self.size == self.size:

        


############################################################################################


class fastLFU:
    def __init__(self, size):
        self.capacity = size
        self.cache = dict()
        self.frequencies = dict()

    def get(self, key):
        if key in self.cache:
            self.frequencies[key] += 1
            return self.cache[key]
        return -1  # If the key is not in the cache

    def add(self, key, value):
        if key in self.cache


def main():
    cache = LFU(4)


if __name__ == "__main__":
    main()
