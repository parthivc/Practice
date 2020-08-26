# https://www.youtube.com/watch?v=XFPHg5KjHoo
# Given an array of integers and a target sum, return the indices of the bounds of the longest subarray 
# that sums to the target sum. Return [-1] if no target sum is reached

import sys


def findLongestSubarrayBySum(data, target):
    left, right, total = 0, 0, 0
    indices = [-1]
    while right < len(data):
        total += data[right]
        while left < right and total > target:
            total -= data[left]
            left -= 1
        if total == target and (len(indices) == 1 or indices[1] - indices[0] < right - left):
            indices = [left + 1, right + 1]
        right += 1
    return indices
    

def main():
    data = [int(elem) for elem in input("Input array: ").split()]
    target = int(input("Enter target sum: "))
    print(findLongestSubarrayBySum(data, target))


if __name__ == '__main__':
    main()
