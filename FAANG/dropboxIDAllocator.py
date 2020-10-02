# ID Allocator with all combinations of runtime

import time
import multiprocessing
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

    def updateTree(self, index, left, right, value):
        if left == right:
            if self.tree[index] == value:
                return False  # If the value was already in the state it was supposed to be
            self.tree[index] = value
            return True  # If the value was correctly changed
        elif (left + right) // 2 >= index:
            self.updateTree(self.left(index), left, (left + right) // 2, value)
        else:
            self.updateTree(self.right(index), (left + right) // 2, right, value)
        self.tree[index] = self.tree[self.left(index)] & self.tree[self.right(index)]

    def getUnallocatedID(self, index, left, right):
        if left == right:
            return right
        elif not self.tree[self.left(index)]:
            return self.getUnallocatedID(self.left(index), left, right // 2)
        elif not self.tree[self.right(index)]:
            return self.getUnallocatedID(self.right(index), (left + right) // 2 + 1, right)

    def allocate(self, _=None):
        if not self.available:
            print("No remaining IDs available")
            return -1
        index = self.getUnallocatedID(1, 0, self.size)
        self.updateTree(index, 0, self.size, 1)
        self.available -= 1
        return index

    def release(self, index):
        if self.updateTree(index, 0, self.size, 0):
            self.available += 1


def main():
    idCount = 10 ** 5

    processCount = max(2, round(math.log10(idCount)) - 2)
    print("\nAllocating IDs concurrently, using {} processes".format(processCount))
    newAllocator = idAllocator(10 ** 6)
    startTime = time.time()
    pool = multiprocessing.Pool(processes=processCount)
    ids = pool.map(newAllocator.allocate, range(idCount))
    pool.map(newAllocator.release, ids)
    duration = time.time() - startTime
    print("IDs allocated: {}\nTime Taken: {:.4f} seconds".format(idCount, duration))

    print("\nAllocating IDs synchronously")
    startTime = time.time()
    allocator = idAllocator(10 ** 6)
    ids = [allocator.allocate() for _ in range(idCount)]
    for i in ids:
        allocator.release(i)
    duration = time.time() - startTime
    print("IDs allocated: {}\nTime Taken: {:.4f} seconds\n".format(idCount, duration))


if __name__ == "__main__":
    main()
