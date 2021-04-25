# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/


def mergeSortedArrays(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    
    # Iterate backwards through arr2
    for index in range(l2 - 1, -1, -1):
        
        # Store the original back to see if anything was swapped
        originalBack = arr1[l1 - 1]

        # Find the smallest element greater than arr2[index]
        runner = l1 - 2
        while runner > -1 and arr1[runner] > arr2[index]:
            # Shifting arr1 to the right if it has bigger elements than the index of arr2
            arr1[runner + 1] = arr1[runner]
            runner -= 1

        if runner != l1 - 2 or originalBack > arr2[index]:
            arr1[runner + 1] = arr2[index]
            arr2[index] = originalBack


def main():
    test1 = [1, 5, 9, 10, 15, 20] 
    test2 = [2, 3, 8, 13]
    result1 = [1, 2, 3, 5, 8, 9]
    result2 = [10, 13, 15, 20]
    print("\nBefore Merging: {} {}".format(test1, test2))
    mergeSortedArrays(test1, test2)
    print("After Merging:  {} {}\n".format(test1, test2))
    assert test1 == result1
    assert test2 == result2
    

    test3 = [1, 3, 4, 5]
    test4 = [2, 4, 6, 8]
    result3 = [1, 2, 3, 4]
    result4 = [4, 5, 6, 8]
    print("Before Merging: {} {}".format(test3, test4))
    mergeSortedArrays(test3, test4)
    print("After Merging:  {} {}\n".format(test3, test4))
    assert test3 == result3
    assert test4 == result4


if __name__ == "__main__":
    main()