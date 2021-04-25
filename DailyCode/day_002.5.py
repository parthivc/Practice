# Return a new sorted merged list from K sorted lists, each with size N


import heapq


def validateLists(lists):
    return not any(any(data[i] > data[i + 1] for i in range(len(data) - 1)) for data in lists)


def mergeSortedLists(lists):
    heap = [(subList[0], index, 1) for index, subList in enumerate(lists) if subList]
    heapq.heapify(heap)
    sortedLists = []
    while heap:
        value, listNum, index = heapq.heappop(heap)
        sortedLists.append(value)
        if index != len(lists[listNum]):
            heapq.heappush(heap, (lists[listNum][index], listNum, index + 1))
    return sortedLists


def main():
    num = int(input("\nNumber of lists: "))
    lists = [list(map(int, input("List {}: ".format(count + 1)).split())) for count in range(num)]
    if validateLists(lists):
        print("\n{}\n".format(mergeSortedLists(lists)))
    else:
        print("\nLists were not sorted, aborting now\n")


if __name__ == "__main__":
    main()
