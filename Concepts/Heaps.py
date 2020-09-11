# The easy and hard way of implementing a heap (support for min and max heap)

##############################################################################################

import heapq, time

class easyHeap:

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

##############################################################################################

class hardHeap:

    def __init__(self, minMax, values=[]):
        self.min = not bool(minMax)  # 1 is maxHeap, 0 is minHeap
        self.heap = values
        if self.heap:
            if self.min:
                self.heap = [value * -1 for value in self.heap]
            self.heapify()
    
    def heapify(self):
        for start in range((len(self.heap) - 2) // 2, -1, -1):
            self.heapDown(start, len(self.heap))
        
    def heapDown(self, start, end):
        root = start
        left = 2 * start + 1
        right = 2 * start + 2
        if left < end and self.heap[root] < self.heap[left]:
            root = left
        if right < end and self.heap[root] < self.heap[right]:
            root = right
        if root != start:
            self.heap[root], self.heap[start] = self.heap[start], self.heap[root]
            self.heapDown(root, end)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def push(self, value):
        if self.min:
            value *= -1
        self.heap.append(value)
        self.heapify()
    
    def pop(self):
        value = self.heap.pop(0)
        if self.min:
            value *= -1
        self.heapify()
        return value

##############################################################################################

def main(Heap):
    startTime = time.time()
    print(Heap.heap)
    Heap.push(50)
    Heap.push(0)
    n = len(Heap.heap)
    for _ in range(n):
        print(Heap.pop())
    endTime = time.time() - startTime
    print("\nThe total time taken for all operation is {} seconds\n".format(endTime * 10000))


if __name__ == "__main__":
    print("\nEasy Heap Testing (Min Heap)\n")
    main(easyHeap(0, [99, 80, 85, 17, -1, 30, 84, 2, 16, 1]))
    print("Hard Heap Testing (Min Heap)\n")
    main(hardHeap(0, [99, 80, 85, 17, -1, 30, 84, 2, 16, 1]))
