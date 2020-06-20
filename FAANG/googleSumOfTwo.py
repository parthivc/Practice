# https://www.youtube.com/watch?v=sfuZzBLPcx4
# Given two arrays of integers, return true if one element from each array sums to a target

import sys


def sumOfTwo(a1, a2, target):
    complements = set()
    for elem in a1:
        complements.add(target - elem)
    for elem in a2:
        if elem in complements:
            return True
    return False


def main():
    a1 = list(map(int, input("Array 1: ").split()))
    a2 = list(map(int, input("Array 2: ").split()))
    target = int(input("Target: "))
    print(sumOfTwo(a1, a2, target))

if __name__ == "__main__":
    main()
