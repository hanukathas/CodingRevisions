def rod_cutting(prices: list, n: int):
    """
        base case is length is 0, return 0
        if length is 1 return the first element from prices

        for a given cut, calculate all cuts from the previous cut made.
        the previous cut was made by maximizing the profit.

    :param prices:
    :param n:
    :return:
    """
    dp = [0] * (n+1)
    for i in range(1, n+1):
        max_profit = float('-inf')
        for j in range(i):
            max_profit = max(max_profit, dp[i-j-1] + prices[j])
        dp[i] = max_profit

    return dp[n]

if __name__ == '__main__':
    print(rod_cutting([1,3,5], 3))
