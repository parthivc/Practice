# Buy and sell a single stock to maximize profit

def maxProfit1(prices):
    if len(prices) < 2:
        return 0
    maxProfit, lowestStock = float('-inf'), prices[0]
    for price in prices:
        maxProfit = max(maxProfit, price - lowestStock)
        lowestStock = min(lowestStock, price)
    return maxProfit

################################################################################################

# Buy and sell multiple stocks to maximize profit

def maxProfit2(prices):
    profit = 0
    for index in range(1, len(prices)):
        profit += max(prices[index] - prices[index - 1], 0)
    return profit

################################################################################################

# Buy and sell up to two stocks to maximize profit (no double buying / selling)

def maxProfit3(prices):
    buy1, sell1 = float('-inf'), 0
    buy2, sell2 = float('-inf'), 0
    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, price + buy2)
    return sell2

################################################################################################

# Buy and sell up to k stocks to maximize profit (no double buying / selling)

def maxProfit4(k, prices):
    if len(prices) < 2 or k < 1:
        return 0
    # If k is greater than the maximum amount of trades, perform maxProfit2 as normal
    if k > len(prices) // 2:
        profit = 0
        for index in range(1, len(prices)):
            profit += max(prices[index] - prices[index - 1], 0)
        return profit
    buy = [float('-inf')] * k
    sell = [0] * k
    for price in prices:
        for index in range(k):
            buy[index] = max(buy[index], (sell[index - 1] if index else 0) - price)
            sell[index] = max(sell[index], buy[index] + price)
    return sell[-1]

################################################################################################

# Buy and sell multiple stocks to maximize profit, with a 1 day cooldown in between transactions

# Simpler but linear space solution

def maxProfitCooldown(prices):
    size = len(prices)
    if size < 2:
        return 0
    buy = [float('-inf')] * size
    sell = [0] * size
    for index in range(size):
        buy[index] = max((buy[index - 1] if index else -prices[0]), (sell[index - 2] if index > 1 else 0) - prices[index])
        sell[index] = max((sell[index - 1] if index else 0), (buy[index - 1] if index else -prices[0]) + prices[index])
    return sell[-1]

# Complex but constant space solution

def maxProfitCooldownConstantSpace(prices):
    size = len(prices)
    if size < 2:
         return 0
    buy0, sell0, buy1, sell1, sell2 = 0, 0, 0, 0, 0
    buy1 = -prices[0]
    buy0 = max(buy1, -prices[1])
    sell0 = max(sell1, buy1 + prices[1])
    sell2 = sell1
    sell1 = sell0
    buy1 = buy0
    for price in prices[2:]:
        buy0 = max(buy1, sell2 - price)
        sell0 = max(sell1, buy1 + price)
        sell2 = sell1
        sell1 = sell0
        buy1 = buy0
    return sell0

# Buy and sell multiple stocks to maximize profit, with a transaction fee for every trade made

def maxProfitFee(fee, prices):
    size = len(prices)
    if size < 2:
        return 0
    buy = [0] * size
    sell = buy[:]
    buy[0] = -prices[0] - fee
    for index in range(1, size):
        buy[index] = max(buy[index - 1], sell[index - 1] - prices[index] - fee)
        sell[index] = max(sell[index - 1], buy[index - 1] + prices[index])
    return sell[-1]
