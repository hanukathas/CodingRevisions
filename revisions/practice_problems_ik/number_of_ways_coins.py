def number_of_ways(coins, amount):
    dp = [0] * (amount+1)
    dp[0] = 0
    print(dp)
    for i in range(1,amount+1):
        total_ways = 0
        if i in coins:

            print(i, dp[i - 1])
            if amount % i == 0:
                total_ways = 1 + dp[i - 1]
                dp[i] = total_ways
            if amount % i != 0:
                total_ways = 1
                dp[i] = total_ways + dp[i - 1]
        else:
            print(i, dp[i-1])
            total_ways = dp[i - 1]
            dp[i] = total_ways

    print(dp)


if __name__ == '__main__':
    print(number_of_ways([9, 1, 8, 10, 3],12))

