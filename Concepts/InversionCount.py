# This is a modified version of merge sort that counts the total number of inversions
# required to make an unsorted array into a sorted array


# Time Complexity:
# O(n log(n))

# Space Complexity:
# O(n)

def mergeSort(array, swap, left, right):
    inversions = 0
    if left < right:
        midPoint = (left + right) // 2
        inversions += mergeSort(array, swap, left, midPoint)
        inversions += mergeSort(array, swap, midPoint + 1, right)
        l, r, i = left, midPoint + 1, left
        while l <= midPoint and r <= right:
            if array[l] <= array[r]:
                swap[i] = array[l]
                l += 1
            else:
                swap[i] = array[r]
                inversions += (midPoint - l + 1)  
                r += 1
            i += 1
        while l <= midPoint:
            swap[i] = array[l]
            i += 1
            l += 1
        while r <= right:
            swap[i] = array[r]
            i += 1
            r += 1
        for x in range(left, right + 1):
            array[x] = swap[x]
    return inversions


def getInversions(array):
    return mergeSort(array, [0] * len(array), 0, len(array) - 1)


def efficientInversions(array):
    length = len(array)
    if length == 1:
        return 0
    mid = length // 2
    right = array[:mid]
    left = array[mid:]
    inversions = efficientInversions(right) + efficientInversions(left)
    leftBound = length - mid
    r = 0
    l = 0
    for i in range(length):
        if r < mid and (l >= leftBound or right[r] <= left[l]):
            array[i] = right[r]
            inversions += l
            r += 1 
        elif l < leftBound:
            array[i] = left[l]
            l += 1
    return inversions
    

def main():
    tests = [
        [1, 20, 6, 4, 5],
        [8, 4, 2, 1],
        [3, 1, 2]
    ]
    print()
    for test in tests:
        preSort = test[:]
        result = efficientInversions(test)
        print("Array:\t\t{}\nSorted array:\t{}\nInversions:\t{}\n".format(preSort, test, result))


if __name__ == "__main__":
    main()
