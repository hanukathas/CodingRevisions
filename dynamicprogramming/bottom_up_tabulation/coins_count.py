def coin_change_bottom_up(coins, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    print(dp)

    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[value] if dp[value] != float('inf') else -1

if __name__ == '__main__':
    print(coin_change_bottom_up([1,3,5], 9))