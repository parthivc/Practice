# This implementation calculates the minimum number of swaps required to make the array sorted

def minimumSwaps(array):
    table = dict()
    for index, val in enumerate(array):
        table[val] = index
    sortedArray = sorted(array)
    swaps = 0
    for index in range(len(array)):
        if array[index] != sortedArray[index]:
            swapIndex = table[sortedArray[index]]
            table[array[index]] = table[sortedArray[index]]
            array[index], array[swapIndex] = sortedArray[index], array[index]
            swaps += 1
    return swaps


def main():
    tests = [
        [1, 20, 6, 4, 5],
        [8, 4, 2, 1],
        [3, 1, 2]
    ]
    print()
    for test in tests:
        preSort = test[:]
        result = minimumSwaps(test)
        print("Array:\t\t{}\nSorted array:\t{}\nSwaps:\t\t{}\n".format(preSort, test, result))


if __name__ == "__main__":
    main()
