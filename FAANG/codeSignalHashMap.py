# Hash Map Code Signal Problem

import time


def newNaive(queryType, query):
    table = {}
    getSum = 0
    for q, v in zip(queryType, query):
        if q == "insert":
            table[v[0]] = v[1]
        if q == "get":
            getSum += table[v[0]]
        if v[0] != 0:
            if q == "addToKey":
                tmp = dict()
                for key in list(table.keys()):
                    tmp[key + v[0]] = table[key]
                table = tmp
            if q == "addToValue":
                for key in list(table.keys()):
                    table[key] += v[0]
    return getSum


def backwards(queryType, query):
    getSum = 0
    getTable = dict()
    keyAdd = 0
    for index in range(len(query) - 1, -1, -1):
        command, value = queryType[index], query[index]
        if command == "get":
            # For overlapping get calls
            if keyAdd != 0:
                tmp = dict()
                for key in list(getTable.keys()):
                    tmp[key - keyAdd] = getTable[key]
                getTable = tmp
                keyAdd = 0
            if value[0] in getTable:
                getTable[value[0]] += 1
            else:
                getTable[value[0]] = 1  # frequency
        elif getTable:
            if command == "addToKey":
                keyAdd += value[0]
            elif command == "addToValue":
                getSum += value[0] * sum([getTable[key] for key in getTable])
            elif command == "insert":
                tmp = dict()
                for key in list(getTable.keys()):
                    tmp[key - keyAdd] = getTable[key]
                getTable = tmp
                keyAdd = 0
                if value[0] in getTable:
                    getSum += value[1] * getTable[value[0]]
                    getTable.pop(value[0])
    return getSum
        

def main():
    t1 = ["insert", "insert", "addToValue", "addToKey", "get"]
    q1 = [[1, 2], [2, 3], [2], [1], [3]]
    t2 = ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"]
    q2 = [[1, 2], [2], [1], [2, 3], [1], [-1], [3]]
    t3 = ["addToValue", "addToKey", "addToKey", "insert", "addToValue", "addToValue", "insert", "get", "get", "insert"]
    q3 = [[-2], [-3], [0], [-3, 1], [-2], [-4], [2, -4], [2], [2], [3, -1]]

    #################################################################################################################################

    startTime = time.time()
    result = newNaive(t1, q1)
    endTime = time.time() - startTime
    print("\nnewNaive output: {}\nExpected Output: {}\nTime Taken: {:.8f}".format(result, 5, endTime * 100000))
    startTime = time.time()
    result = newNaive(t2, q2)
    endTime = time.time() - startTime
    print("\nnewNaive output: {}\nExpected Output: {}\nTime Taken: {:.8f}".format(result, 6, endTime * 100000))
    startTime = time.time()
    result = newNaive(t3, q3)
    endTime = time.time() - startTime
    print("\nnewNaive output: {}\nExpected Output: {}\nTime Taken: {:.8f}\n".format(result, -8, endTime * 100000))

    #################################################################################################################################

    startTime = time.time()
    result = backwards(t1, q1)
    endTime = time.time() - startTime
    print("\n\n\nbackwards output: {}\nExpected Output: {}\nTime Taken: {:.8f}".format(result, 5, endTime * 100000))
    startTime = time.time()
    result = backwards(t2, q2)
    endTime = time.time() - startTime
    print("\nbackwards output: {}\nExpected Output: {}\nTime Taken: {:.8f}".format(result, 6, endTime * 100000))
    startTime = time.time()
    result = backwards(t3, q3)
    endTime = time.time() - startTime
    print("\nbackwards output: {}\nExpected Output: {}\nTime Taken: {:.8f}\n".format(result, -8, endTime * 100000))


if __name__ == "__main__":
    main()
