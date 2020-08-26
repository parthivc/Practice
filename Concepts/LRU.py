# The easy and hard way of implementing a Least Recently Used cache in Python3
# All operations have O(1) time complexity

##############################################################################################

# The following code is the easy implementation method
# This implementation relies on the inbuilt OrderedDict object in Python3

from collections import OrderedDict
import time  # For timing testing

class easyLRU:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1
    
    def add(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

##############################################################################################

# The following code is the hard implementation method
# This implementation relies on a hashtable and a doubly-linked list

class Node:

    def __init__(self, key, value, tail=None, head=None):
        self.key = key
        self.value = value
        self.prev = tail
        self.next = head

class hardLRU:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addToFront(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node
    
    def get(self, key):
        if key in self.map:
            current = self.map[key]
            value = current.value
            self.deleteNode(current)
            self.addToFront(current)
            return value
        return -1

    def add(self, key, value):
        if key in self.map:
            current = self.map[key]
            current.value = value
            self.deleteNode(current)
            self.addToFront(current)
        else:
            node = Node(key, value)
            self.map[key] = node
            if self.size < self.capacity:
                self.size += 1
                self.addToFront(node)
            else:
                self.map.pop(self.tail.prev.key)
                self.deleteNode(self.tail.prev)
                self.addToFront(node)

##############################################################################################

def main(LRU):
    startTime = time.time()
    LRU.add(1, 10)
    LRU.add(2, 20)
    print("Value for the key 1 is {}".format(LRU.get(1)))
    LRU.add(3, 30)
    print("Value for the key 2 is {}".format(LRU.get(2)))
    LRU.add(4, 40)
    print("Value for the key 1 is {}".format(LRU.get(1)))
    print("Value for the key 3 is {}".format(LRU.get(3)))
    print("Value for the key 4 is {}".format(LRU.get(4)))
    endTime = time.time() - startTime
    print("\nThe total time taken for all operation is {} seconds\n".format(endTime))


if __name__ == "__main__":
    print("\nEasy LRU Testing\n")
    main(easyLRU(2))
    print("Hard LRU Testing\n")
    main(hardLRU(2))
    