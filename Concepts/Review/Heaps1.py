# Review of heaps implementation


import heapq
import time

class easyHeap:

    def __init__(self, values=[], maxHeap=0):
        self.values = values
        self.maxHeap = maxHeap
        if self.values:
            if self.maxHeap:
                self.values = [value * -1 for value in values]
            self.heapify()
    
    def push(self, value):
        if self.maxHeap:
            value *= -1
        heapq.heappush(self.values, value)

    def pop(self):
        value = heapq.heappop(self.values)
        if self.maxHeap:
            value *= -1
        return value

    def heapify(self):
        heapq.heapify(self.values)

    def heapsort(self):
        self.values = [self.pop() for _ in range(len(self.values))]

###################################################################

class hardHeap:

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

    def heapDown(self, root):
        parent = root
        left = parent * 2 + 1
        right = parent * 2 + 2
        if left < self.size and self.values[parent] > self.values[left]:
            parent = left
        if right < self.size and self.values[parent] > self.values[right]:
            parent = right
        if parent != root:
            self.values[parent], self.values[root] = self.values[root], self.values[parent]
            self.heapDown(parent)

    def heapsort(self):
        self.values = [self.pop() for _ in range(self.size)]


def main(Heap):
    startTime = time.time()
    print(Heap.values)
    Heap.push(50)
    Heap.push(0)
    print(Heap.values)
    Heap.heapsort()
    print(Heap.values)
    endTime = time.time() - startTime
    print("\nThe total time taken for all operation is {} seconds\n".format(endTime * 10000))


if __name__ == "__main__":
    print("\nEasy Heap Testing (Min Heap)\n")
    main(easyHeap([99, 80, 85, 17, -1, 30, 84, 2, 16, 1]))
    print("Hard Heap Testing (Min Heap)\n")
    main(hardHeap([99, 80, 85, 17, -1, 30, 84, 2, 16, 1]))
