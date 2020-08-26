# Given a set of intervals, find the maximum number of overlapping intervals at any point in time

def maximumOverlappingIntervals(intervals):
    maxOverlaps, current = 0, 0
    table = []
    for index in range(len(intervals)):
        table.append([intervals[index][0], True])
        table.append([intervals[index][1], False])
    sortedTable = sorted(table)
    for index in range(len(sortedTable)):
        print(sortedTable[index])
        if sortedTable[index][1]:
            current += 1
        if not sortedTable[index][1]:
            current -= 1
        maxOverlaps = max(current, maxOverlaps)
    return maxOverlaps


def main():
    tests = [
        [[1, 2], [2, 4], [3, 6]]
    ]
    print()
    for test in tests:
        result = maximumOverlappingIntervals(test)
        print("Intervals:\t\t\t{}\nMaximum Overlapping Intervals:\t{}\n".format(test, result))


if __name__ == "__main__":
    main()