# https://www.youtube.com/watch?v=IdZlsG6P17w
# Rotate a square matrix 90°
# NOTE: Intentionally not performing a pythonic list comprehension

import sys


def rotateImage(data):
    size = len(data)
    # Transpose
    for i in range(size):
        for j in range(i, size):
            data[i][j], data[j][i] = data[j][i], data[i][j]
    # Horizontal flip
    for i in range(size):
        for j in range(size // 2):
            data[i][j], data[i][size - 1 - j] = data[i][size - 1 - j], data[i][j]
    return data


def main():
    data = list()
    data.append(list(map(int, input("Row 0: ").split())))
    for index in range(len(data[0]) - 1):
        data.append(list(map(int, input("Row {}: ".format(index + 1)).split())))
    print(rotateImage(data))


if __name__ == "__main__":
    main()
