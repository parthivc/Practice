# Implementation of a Priority Queue in many ways

# The easy way:

from queue import PriorityQueue

###############################################################

# The slightly harder way:

import heapq

class easyPQ:

    def __init__(self, minMax, values=[]):
        self.max = bool(minMax)  # 1 is maxHeap, 0 is minHeap
        self.heap = values
        if self.heap:
            if self.max:
                self.heap = [value * -1 for value in self.heap]
            self.heapify()

    def push(self, value):
        if self.max:
            value *= -1
        heapq.heappush(self.heap, value)

    def pop(self):
        value = heapq.heappop(self.heap)
        if self.max:
            value *= -1
        return value

    def heapify(self):
        heapq.heapify(self.heap)

# The hard way:

class hardPQ:

    def __init__(self, values=[], maxHeap=0):
        self.values = values
        self.size = len(values)
        self.maxHeap = maxHeap
        if self.values:
            if self.maxHeap:
                self.values = [value * -1 for value in values]
            self.heapify()
    
    def push(self, value):
        if self.maxHeap:
            value *= -1
        self.values.append(value)
        self.size += 1
        self.heapify()

    def pop(self):
        value = self.values.pop(0)
        if self.maxHeap:
            value *= -1
        self.size -= 1
        self.heapify()
        return value

    def heapify(self):
        for root in range(len(self.values) // 2, -1, -1):
            self.heapDown(root)

    def compare(self, a, b):
        if type(self.values[a]) is tuple and type(self.values[b]) is tuple:
            return self.values[a][0] > self.values[b][0]
        return self.values[a] > self.values[b]

    def heapDown(self, root):
        parent = root
        left = parent * 2 + 1
        right = parent * 2 + 2
        if left < self.size and self.compare(left, root):
            parent = left
        if right < self.size and self.compare(right, root):
            parent = right
        if parent != root:
            self.values[parent], self.values[root] = self.values[root], self.values[parent]
            self.heapDown(parent)

    def heapsort(self):
        self.values = [self.pop() for _ in range(self.size)]


# if __name__ == "__main__":
#     main()
