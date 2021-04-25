# https://www.youtube.com/watch?v=5co5Gvp_-S0
# Given an array of characters, find the first non repeating character
# Return _ if all characters are repeating


# Technically O(N^2) because array.rindex are O(N) operations
# O(N^2) time and O(1) space
def firstNonRepeatingCharacterN2(data):
    data = ''.join(data)
    for index, elem in enumerate(data):
        if index == data.rindex(elem):
            return elem
    return '_'


# O(1) space and O(N) time
def firstNonRepeatingCharacterN(data):
    charCounts = [0] * 26
    startOrd = ord('a')
    # If characters are not all lower case
    for index in range(len(data)):
        data[index] = data[index].lower()
        charCounts[ord(data[index]) - startOrd] += 1
    for elem in data:
        if charCounts[ord(elem) - startOrd] == 1:
            return elem
    return '_'


# If there is only one non repeating character
def firstNonRepeatingCharacter(data):
    asciiCounter = 0
    for elem in data:
        asciiCounter ^= ord(elem)
    return chr(asciiCounter)


def main():
    data = input("Input char array: ").split()
    print(firstNonRepeatingCharacterN(data))


if __name__ == '__main__':
    main()
