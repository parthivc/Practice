# https://www.youtube.com/watch?v=4eWKHLSRHPY
# Given an array of sorted integers, return an array of their sorted squares

import sys


def sortedSquareArray(data):
    sortedSquares = [0] * len(data)
    left, right = 0, len(data) - 1
    for index in range(len(data) - 1, -1, -1):
        if abs(data[left]) > data[right]:
            sortedSquares[index] = data[left] ** 2
            left += 1
        else:
            sortedSquares[index] = data[right] ** 2
            right -= 1
    return sortedSquares


def main():
    data = [int(elem) for elem in input("Input array: ").split()]
    print(sortedSquareArray(data))


if __name__ == '__main__':
    main()
