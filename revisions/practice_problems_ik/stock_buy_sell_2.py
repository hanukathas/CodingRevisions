import heapq


def stock_buy_sell_2(prices: list):
    min_price_index = 0
    profit = 0

    for i in range(1, len(prices)):
        if prices[min_price_index] <= prices[i]:
            profit += prices[i] - prices[min_price_index]

        min_price_index = i
    return profit


def stock_buy_sell_3(prices: list):
    if not prices:
        return 0

        # Initialize variables for first and second buy/sell
    first_buy = float('inf')
    first_profit = 0
    second_buy = float('inf')
    second_profit = 0

    for price in prices:
        # Update first buy to minimize cost
        first_buy = min(first_buy, price)
        # Update first profit to maximize profit after first transaction
        first_profit = max(first_profit, price - first_buy)
        # Update second buy to minimize cost (considering profit from first trade)
        second_buy = min(second_buy, price - first_profit)
        # Update second profit to maximize total profit
        second_profit = max(second_profit, price - second_buy)

        # print(first_buy, first_profit, second_buy, second_profit)

    return second_profit

def stock_buy_sell_3_r(prices: list, k: int):
    if not prices:
        return 0
    first_buy = float('inf')
    second_buy = float('inf')
    first_profit = 0
    second_profit = 0

    profits = []
    for price in prices:
        first_buy = min(first_buy, price)
        first_profit = max(first_profit, price - first_buy)

        second_buy = min(second_buy, price - first_profit)
        net = price - second_buy
        if second_profit < net:
            profits.append(net)
            second_profit = net

    print(profits)
    return second_profit

def maxProfit_4( prices: list, k: int) -> int:
    if not prices or k == 0:
        return 0
    if k > len(prices) // 2:
        return sum(max(0, prices[i] - prices[i-1]) for i in range(len(prices)))
    dp = [[0] * (k + 1) for _ in range(len(prices))]
    for j in range(1, k+1):
        local_max = -prices[0]
        for i in range(1, len(prices)):
            dp[i][j] = max(dp[i-1][j], prices[i] + local_max)
            local_max = max(local_max, dp[i-1][j-1] - prices[i])
    return dp[-1][k]


if __name__ == '__main__':
    # print(stock_buy_sell_2([7, 1, 5, 3, 6, 4]))
    # print(stock_buy_sell_2([1, 2, 3, 4, 5]))
    # print(stock_buy_sell_2([7, 6, 4, 3, 1]))
    # print(stock_buy_sell_3_r([3, 3, 5, 0, 0, 3, 1, 4]))
    # print(stock_buy_sell_3_r([1, 2, 3, 4, 5]))
    # print(stock_buy_sell_3_r([7, 6, 4, 3, 1]))
    # print(stock_buy_sell_3_r([6, 1, 3, 2, 4, 7]))
    # print(stock_buy_sell_3([1,4,2]))
    # print(stock_buy_sell_3_r([1, 4, 2]))
    print(stock_buy_sell_3_r([3,2,6,5,0,3], 2))
    print(maxProfit_4([6,1,3,2,4,7], 1))
