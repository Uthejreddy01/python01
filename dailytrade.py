def max_profit(prices):
    if not prices:
        return 0
    n = len(prices)
    max_profit_1 = [0] * n
    max_profit_2 = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        max_profit_1[i] = max(max_profit_1[i - 1], prices[i] - min_price)
    max_price = prices[n - 1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        max_profit_2[i] = max(max_profit_2[i + 1], max_price - prices[i])
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, max_profit_1[i] + max_profit_2[i])
    return max_profit
test_cases = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [10, 22, 5, 75, 65, 80],
    [2, 30, 15, 10, 8, 25, 80],
    [5, 25, 3, 10, 7, 9]
]
for prices in test_cases:
    print(max_profit(prices))