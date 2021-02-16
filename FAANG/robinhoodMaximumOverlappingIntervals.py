# Given a set of intervals, find the maximum number of overlapping intervals at any point in time

def maximumOverlappingIntervals(intervals):
    maxOverlaps, current = 0, 0
    table = []
    for index in range(len(intervals)):
        table.append([intervals[index][0], True])
        table.append([intervals[index][1], False])
    sortedTable = sorted(table)
    for index in range(len(sortedTable)):
        if sortedTable[index][1]:
            current += 1
        if not sortedTable[index][1]:
            current -= 1
        maxOverlaps = max(current, maxOverlaps)
    return maxOverlaps

def maximumOverlappingIntervalsNoSpace(intervals):
    result = 0
    current = 0
    start = 0
    end = 0
    intervals.sort()
    while start < len(intervals) and end < len(intervals):
        if intervals[start][0] < intervals[end][1]:
            current += 1
            result = max(result, current)
            start += 1
        else:
            current -= 1
            end += 1
    return result



def main():
    tests = [
        [[1, 2], [2, 4], [3, 6]], 
        [[0, 2], [1, 5], [3, 6], [4, 7], [7, 8]]
    ]
    print()
    for test in tests:
        result = maximumOverlappingIntervals(test)
        result2 = maximumOverlappingIntervalsNoSpace(test)
        print("Intervals:\t\t\t{}\nMaximum Overlapping Intervals:\t{}\n".format(test, result))
        print("Intervals:\t\t\t{}\nMaximum Overlapping Intervals:\t{}\n".format(test, result2))


if __name__ == "__main__":
    main()