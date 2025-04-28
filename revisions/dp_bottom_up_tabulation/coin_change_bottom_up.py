def coin_change_bottom_up(coins: list, value: int):
    dp = [float('inf')] * (value+1)
    dp[0] = 0
    for val in range(1, value+1):
        for coin in coins:
            if coin <= val:
                dp[val] = min(dp[val], dp[val - coin] + 1)

    return dp[value] if dp[value] != float('inf') else -1

def coin_change_bottom_up_r(coins: list, value: int):
    """
    https://leetcode.com/problems/coin-change/description/
    :param coins:
    :param value:
    :return:
    """

    dp = [float('inf') * (value + 1)]
    dp[0] = 0

    for i in range(1, value+1):
        for coin in coins:
            if i <= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[value] if dp[value] != float('inf') else -1


if __name__ == '__main__':
    print(coin_change_bottom_up([1,5,10], 72))

