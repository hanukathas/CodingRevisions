def money_sums(n, coins):
    total_sum = sum(coins)
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for coin in coins:
        for j in range(total_sum, coin - 1, -1):
            if dp[j - coin]:
                dp[j] = True
    print(dp)


if __name__ == '__main__':
    n = 4
    coins = [4, 2, 5, 2]
    money_sums(n, coins)