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


def beautifyArray(array):
    # This works if the array needs to be sorted but can be returned in either direction
    return min(minimumSwaps(array[:]), minimumSwaps(list(reversed(array[:]))))


def main():
    tests = [
        [3, 4, 2, 5, 1],
        [1, 20, 6, 4, 5],
        [8, 4, 2, 1],
        [3, 1, 2]
    ]
    print()
    for test in tests:
        preSort = test[:]
        result = minimumSwaps(test)
        minBeautifulSwaps = beautifyArray(test)
        print("Array:\t\t\t{}\nSorted array:\t\t{}\nSwaps:\t\t\t{}\nBeautiful Swaps:\t{}\n".format(preSort, test, result, minBeautifulSwaps))


if __name__ == "__main__":
    main()