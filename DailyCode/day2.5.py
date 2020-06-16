# Return a new sorted merged list from K sorted lists, each with size N


def main():
    num = int(input("Number of lists"))
    lists = []
    for count in range(num):
        data = list(map(int, input("List {}: ".format(count + 1)).split()))
        lists.append(data)
    validateLists(lists)
