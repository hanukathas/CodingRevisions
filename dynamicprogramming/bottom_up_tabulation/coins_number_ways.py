def coin_change_count(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] = dp[j] + dp[j - coin]

    return dp[amount]

if __name__ == '__main__':
    print(coin_change_count([5], 6))

