# https://www.youtube.com/watch?v=XSdr_O-XVRQ
# Given an array of positive integers where the maximum value is the length of the array,
# Find the first duplicate value in the array, return -1 if there are no duplicates

import sys


def firstDuplicate(array):
    for index in range(len(array)):
        if array[abs(array[index]) - 1] < 0:  # Duplicate has been found
            return abs(array[index])
        else:
            array[abs(array[index]) - 1] *= -1
    return -1


def main():
    data = [int(elem) for elem in input("Input array: ").split()]
    print(firstDuplicate(data))


if __name__ == '__main__':
    main()
