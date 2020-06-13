# https://www.youtube.com/watch?v=5co5Gvp_-S0
# Given an array of characters, find the first non repeating character
# Return _ if all characters are repeating

import sys


def firstNonRepeatingCharacter(data):
    data = ''.join(data)
    for elem in data:
        if data.index(elem) == data.rindex(elem):
            return elem
    return '_'


def main():
    data = input("Input array: ").split()
    print(firstNonRepeatingCharacter(data))


if __name__ == '__main__':
    main()