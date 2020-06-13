# Given a list of numbers and a number k, return whether any two numbers from the list add up to k

import sys


def day1(data, target):
    complements = set()
    for elem in data:
        if elem in complements:
            return True
        complements.add(target - elem)
    return False


def main():
    data = list(map(int, input("Enter array: ").split()))
    target = int(input("Enter target: "))
    print(day1(data, target))


if __name__ == "__main__":
    main()
