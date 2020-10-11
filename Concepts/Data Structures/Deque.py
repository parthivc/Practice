from collections import deque
import sys


def slidingWindow(array, windowSize):
    d = deque()
    result =  -sys.maxsize - 1  # float('-inf')
    for index in range(len(array)):
        if d and index - d[0] == windowSize:
            d.popleft()
        while d and array[d[-1]] > array[index]:
            d.pop()
        d.append(index)
        if index >= windowSize - 1:
            result = max(result, array[d[0]])
    return result


def main():
    # Running dropbox round 1 question as a performance example
    # Find the maximum-minimum value in a window of size n
    n = 3
    test = [4, 5, 6, 1, 2, 3, 7, 8, 9]
    # Assessments = [4, 5, 6, 1, 2, 3, 1, 2, 3]
    print("\nWindow Size: \t{}\nInput: \t\t{}\nResult: \t{}\n".format(n, test, slidingWindow(test, n)))


if __name__ == "__main__":
    main()
