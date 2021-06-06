# Implementation of Quick Select


# This method finds the kth smallest element
# To find the kth largest element, flip all inequality signs except for the while loops

# import random
# def partition(a, l, r, pivotIndex):
#         pivotVal = a[pivotIndex]
#         a[pivotIndex], a[r] = a[r], a[pivotIndex]
#         storeIndex = l
#         for i in range(l, r):
#                 if(a[i] > pivotVal):
#                         a[storeIndex], a[i] = a[i], a[storeIndex]
#                         storeIndex+=1
#         a[r], a[storeIndex] = a[storeIndex], a[r]
#         return storeIndex

# def select(a, l, r, k):
#         if(l == r):
#                 return l
#         pivotIndex = random.randint(l, r)
#         pivotIndex = partition(a, l, r, pivotIndex)
#         if(k == pivotIndex):
#                 return k
#         elif(k < pivotIndex):
#                 return select(a, l, pivotIndex-1, k)
#         else:
#                 return select(a, pivotIndex+1, r, k)


# arr = [12, 40, 20, 10, 45, 13, 53]
# n = len(arr)
# k = 4
# res = select(arr, 0, n-1, k-1)



def quickSelect(nums, k):
    start = 0
    end = len(nums) - 1
    while start <= end:
        pivot = start
        for runner in range(start, end):
            if nums[runner] >= nums[end]:
                nums[runner], nums[pivot] = nums[pivot], nums[runner]
                pivot += 1
        nums[end], nums[pivot] = nums[pivot], nums[end]
        count = end - pivot + 1
        if count < k:
            k -= count
            end = pivot - 1
        elif count > k:
            start = pivot + 1
        else:
            return nums[pivot]

def main():
    array = [10, 4, 5, 8, 6, 11, 26]
    k = 3  # K is 1-indexed
    print("\n{}\nThe kth smallest element with k = {} is".format(array, k), end=" ")
    print("{}\n".format(quickSelect(array, k)))
    array = [-3, -2, -3, -1, -2, -4, -5, -5, -6]
    k = 4  # K is 1-indexed
    print("\n{}\nThe kth smallest element with k = {} is".format(array, k), end=" ")
    print("{}\n".format(quickSelect(array, k)))

if __name__ == "__main__":
    main()
