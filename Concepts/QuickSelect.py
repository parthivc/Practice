# Implementation of Quick Select


# This method finds the kth smallest element
# To find the kth largest element, flip all inequality signs except for the while loops

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


# def recursiveQuickSelect(array, k)


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
