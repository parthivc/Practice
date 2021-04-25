# Implement a hashtable with the following methods: put (insert key-value pair), get (return value given key), 
# addToKey(add argument to all keys in hashmap), addToValue(add offset to all values in hashmap)


class modifiedHashTable:

    def __init__(self):
        self.table = dict()
        self.keyOffset = 0
        self.valueOffset = 0

    def put(self, key, value):
        newKey = key - self.keyOffset
        newValue = value - self.valueOffset
        self.table[newKey] = newValue

    def get(self, key):
        newKey = key - self.keyOffset
        if self.table[newKey]:
            return self.valueOffset + self.table[newKey]

    def addToKey(self, offset):
        self.keyOffset += offset

    def addToValue(self, offset):
        self.valueOffset += offset