# https://www.youtube.com/watch?v=HWW-jA6YjHk
# Given a list of coins and a target sum, return the smallest number of coins required to achieve that sum


def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def listLCM(coins):
    result = coins[0]
    for index in range(1, len(coins)):
        result = lcm(result, coins[index])
    return int(result)

def minCoins(target, coins):
    lcm = listLCM(coins)
    result = 0
    if target > lcm:
        result += (target // lcm) * (lcm // max(coins))
        target %= lcm
    visited = set()
    queue = [(target, ([max(coins)] * result if result else []))]
    depth = 0
    while queue:
        size = len(queue)
        while size != 0:
            current, path = queue.pop(0)
            size -= 1
            if current in visited or current < 0:
                continue
            elif current == 0:
                return depth + result, path
            visited.add(current)
            for coin in coins:
                queue.append((current - coin, path + [coin]))
        depth += 1
    return -1


def main():
    target = int(input("\nInput target sum: "))
    coins = input("Enter custom coins or press enter for defaults: ")
    if coins:
        coins = list(map(int, coins.split()))
    else:
        coins = [25, 10, 5, 1]
    result = minCoins(target, coins)
    table = dict()
    if result == -1:
        print("\nResult not possible\n")
    else:
        for coin in result[1]:
            if coin in table:
                table[coin] += 1
            else:
                table[coin] = 1
        print("\nNumber of coins: {}".format(result[0]))
        print("\nCoin Value | Coin Frequency\n")
        for key in table:
            print("{}\t   |  \t{}".format(key, table[key]))
        print()



if __name__ == "__main__":
    main()
