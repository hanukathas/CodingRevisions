def coin_change_count(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, amount+1):
            dp[j] = dp[j] + dp[j - coin]

    return dp[amount]

def coin_change_count_revision(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] = dp[i] + dp[i - coin]
    return dp[amount]

if __name__ == '__main__':
    print(coin_change_count_revision([1, 2, 5], 6))

