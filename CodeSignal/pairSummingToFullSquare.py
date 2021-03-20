from collections import defaultdict

def pairSummingToFullSquare(arr):
    powers = [x ** 2 for x in range(201)]
    result = 0
    table = defaultdict(int)
    for elem in arr:
        table[elem] += 1
        for p in powers:
            if p - elem in table:
                result += table[p - elem]
    return result


def main():
    test = [-20000, 20000, 0, 1, 4, 9, 16]
    result = pairSummingToFullSquare(test)
    print(result)

if __name__ == '__main__':
    main()