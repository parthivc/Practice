# This is an implementation of merge sort in Python3


# Time Complexity: 
# Ω(n log(n))
# Θ(n log(n))
# O(n log(n))

# Space Complexity:
# O(n)

def mergeSort(array):
    if len(array) > 1:
        midPoint = len(array) // 2
        leftHalf = array[:midPoint]
        rightHalf = array[midPoint:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        l, r, i = 0, 0, 0
        while l < len(leftHalf) and r < len(rightHalf):
            if leftHalf[l] < rightHalf[r]:
                array[i] = leftHalf[l]
                l += 1
            else:
                array[i] = rightHalf[r]
                r += 1
            i += 1
        while l < len(leftHalf):
            array[i] = leftHalf[l]
            i += 1
            l += 1
        while r < len(rightHalf):
            array[i] = rightHalf[r]
            i += 1
            r += 1
        

def main():
    test1 = [12, 11, 13, 5, 6, 7]
    print("\nBefore sort: {}".format(test1))
    mergeSort(test1)
    print("\nAfter sort: {}\n".format(test1))


if __name__ == "__main__":
    main()
