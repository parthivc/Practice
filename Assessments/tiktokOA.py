
def common_elements(arr1, arr2):
    table = dict()
    for elem in arr1:
        if elem in table:
            table[elem] += 1
        else:
            table[elem] = 1
    result = []
    for elem in arr2:
        if elem in table:
            result.append(elem)
            table[elem] -= 1
            if not table[elem]:
                table.pop(elem)
    result.sort()
    return result

# Enter your code here. Read input from STDIN. Print output to STDOUT

caseCount = int(input())
cases = []
for _ in caseCount:
    cases.append(list(map(int, input().split())))
for m1, m2 in cases:
    




def main():
    print("\n")



if __name__ == "__main__":
    main()