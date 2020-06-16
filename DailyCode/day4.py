# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.


def smallestPositiveInt(data):
    size = len(data)
    if size == 0:
        return "Empty list"
    elif size == 1:
        return 2 if data[0] == 1 else 1
    # Move all positive elements to the back of the list
    positiveIndex = 0
    for index in range(size):
        if data[index] < 1:
            data[index], data[positiveIndex] = data[positiveIndex], data[index]
            positiveIndex += 1
    data = data[positiveIndex:]
    size -= positiveIndex
    for index in range(size):
        if abs(data[index]) - 1 < size and data[abs(data[index]) - 1] > 0:
            data[abs(data[index]) - 1] *= -1
    for index in range(size):
        if data[index] > 0:
            return index + 1
    return size + 1


def main():
    data = list(map(int, input("Enter array: ").split()))
    print("\n{}\n".format(smallestPositiveInt(data)))


if __name__ == "__main__":
    main()
