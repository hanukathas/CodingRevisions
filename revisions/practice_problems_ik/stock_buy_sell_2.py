import heapq


def stock_buy_sell_2(prices: list):
    min_price_index = 0
    profit = 0
    profits = []
    for i in range(1, len(prices)):
        if prices[min_price_index] <= prices[i]:
            profit += prices[i] - prices[min_price_index]
            profits.append(profit)
        min_price_index = i
        profit = 0
    print(profits)
    profits.sort(reverse=True)
    final = 0
    if all(profits[i-1] == profits[i] for i in range(len(profits))):
        final = sum(profits)
    else:
        final = sum(profits[:2])
    return final


if __name__ == '__main__':
    print(stock_buy_sell_2([7,1,5,3,6,4]))
    print(stock_buy_sell_2([1,2,3,4,5]))
    print(stock_buy_sell_2([7,6,4,3,1]))
    print(stock_buy_sell_2([3,3,5,0,0,3,1,4]))
    print(stock_buy_sell_2([1,2,3,4,5]))
    print(stock_buy_sell_2([6,1,3,2,4,7]))


