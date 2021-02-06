# ID Allocator with all combinations of runtime

import time
import math


class idAllocator:
    def __init__(self, size):
        self.size = size
        self.available = size
        self.tree = [0 for _ in range(size * 4)]

    def left(self, index):
        return index << 1
    
    def right(self, index):
        return (index << 1) + 1

    def updateTree(self, index, left, right, value, targetID):
        if left == right:
            if self.tree[index] == value:
                return False  # If the value was already in the state it was supposed to be
            self.tree[index] = value
            return True  # If the value was correctly changed
        elif (left + right) // 2 >= targetID:
            self.updateTree(self.left(index), left, (left + right) // 2, value, targetID)
        else:
            self.updateTree(self.right(index), (left + right) // 2 + 1, right, value, targetID)
        self.tree[index] = self.tree[self.left(index)] & self.tree[self.right(index)]

    def getUnallocatedID(self, index, left, right):
        if left == right:
            return right
        elif not self.tree[self.left(index)]:
            return self.getUnallocatedID(self.left(index), left, (left + right) // 2)
        elif not self.tree[self.right(index)]:
            return self.getUnallocatedID(self.right(index), (left + right) // 2 + 1, right)

    def allocate(self, _=None):
        if not self.available:
            print("No remaining IDs available")
            return -1
        targetID = self.getUnallocatedID(1, 0, self.size)
        self.updateTree(1, 0, self.size, 1, targetID)
        self.available -= 1
        return targetID

    def release(self, targetID):
        if self.updateTree(1, 0, self.size, 0, targetID):
            self.available += 1


def main():
    idCount = 10 ** 5

    print("\nAllocating IDs synchronously")
    startTime = time.time()
    allocator = idAllocator(idCount)
    ids = [allocator.allocate() for _ in range(idCount)]
    for i in ids:
        allocator.release(i)
    duration = time.time() - startTime
    print("IDs allocated: {}\nTime Taken: {:.4f} seconds\n".format(idCount, duration))


if __name__ == "__main__":
    main()
