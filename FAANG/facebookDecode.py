import sys


def solve(data, n, memo):
    if n == 0:
        return 1
    s = len(data) - n
    if data[s] == '0':
        return 0
    if memo[n] is not None:
        return memo[n]
    numWays = solve(data, n - 1, memo)
    if n > 1 and int(data[s: s + 2]) < 27:
        numWays += solve(data, n - 2, memo)
    memo[n] = numWays
    return numWays


def num_ways(data):
    return solve(data, len(data), [None] * (len(data) + 1))



def main():
    data = sys.argv[1]
    print(num_ways(data))


if __name__ == "__main__":
    main()
