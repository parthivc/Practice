# Implementation of Quick Select


# This method finds the kth smallest element
# To find the kth largest element, flip all inequality signs except for the while loops

def quickSelect(array, k):
    if k == 0 or k == len(array) - 1:
        return "not possible"
    start = 0
    end = len(array) - 1

    while start < end:
        midpoint = array[(start + end) // 2]
        left = start
        right = end
        while left < right:
            if array[left] >= midpoint:
                array[right], array[left] = array[left], array[right]
                right -= 1
            else:
                left += 1
        if array[left] > midpoint:
            left -= 1
        if k <= left:
            end = left
        else:
            start = left + 1
    return array[k - 1]


# def recursiveQuickSelect(array, k)


def main():
    array = [10, 4, 5, 8, 6, 11, 26]
    k = 3  # K is 1-indexed
    print("\n{}\nThe kth smallest element with k = {} is".format(array, k), end=" ")
    print("{}\n".format(quickSelect(array, k)))

if __name__ == "__main__":
    main()
