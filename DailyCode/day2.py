# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# Try solving without division


def withDivision(data):
    total = 1
    for elem in data:
        total *= elem
    for index in range(len(data)):
        data[index] = total / data[index]
    return data


# Without division
def day2(data):
    size = len(data)
    left, right = [1] * size, [1] * size
    for index in range(size - 1):
        left[index + 1] = left[index] * data[index]
    for index in range(size - 1, 0, -1):
        right[index - 1] = right[index] * data[index]
    for index in range(size):
        data[index] = left[index] * right[index]
    return data


def main():
    data = list(map(int, input("Enter array: ").split()))
    print(day2(data))


if __name__ == "__main__":
    main()
