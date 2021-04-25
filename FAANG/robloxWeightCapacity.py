import time, random

def recur(weights, cap, total_sum, memo):
    if(cap in memo):
        return memo[cap]
    if(cap <= 0 or len(weights) == 0):
        return total_sum
    else:
        res = 0
        for i in range(len(weights)):
            val = weights[i]
            tmp = weights[:]
            tmp.pop(i)
            if(cap - val >= 0):
                res = max(res, recur(tmp, cap-val, total_sum+val, memo))
            else:
                res = max(res, recur(tmp, cap-val, total_sum, memo))
        if(cap not in memo):
            memo[cap] = res
        return memo[cap]

def weightCapacity(weights, maxCapacity):
    memo = {}
    res =  recur(weights, maxCapacity, 0, memo)
    # print(len(memo))
    return res


def newWeightCapacity(weights, maxCapacity):
    combos = set()
    # total = []
    for index, weight in enumerate(weights, 1):
        # p = total[:]
        p = list(combos)
        for combo in p:
            combos.add(combo + weight)
            # total.append(combo + weight)
        # total.append(weight)
        combos.add(weight)
        # print(len(combos), len(total), index)
    # print(len(combos), len(total))
    result = 0
    for weight in combos:
        if weight > result and weight <= maxCapacity:
            result = weight
    return result

def main():
    weights = [random.randint(1, 1000) for x in range(15)]
    #weights = [1,1,1]
    #print(weights)
    maxCapacity = 10 ** 7
    #maxCapacity = 3
    startTime = time.time()
    print("\nResult: {}\nTime Taken: {} seconds\n".format(weightCapacity(weights, maxCapacity), time.time() - startTime))
    startTime = time.time()
    print("\nResult: {}\nTime Taken: {} seconds\n".format(newWeightCapacity(weights, maxCapacity), time.time() - startTime))
    


if __name__ == "__main__":
    main()