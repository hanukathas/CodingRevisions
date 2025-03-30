def coin_change_bottom_up(coins, value):
    dp = [float('inf')] * (value + 1)
    dp[0] = 0
    print(dp)

    for i in range(1, value + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[value] if dp[value] != float('inf') else -1

def coin_change_bottom_up_revision(coins, value):
    dp = [float('inf')] * (value+1)
    dp[0] = 0

    for i in range(1, value+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[value]

def coin_change_bottom_up_revision_2(coins, value):
    dp = [float('inf')] * (value+1)
    dp[0] = 0
    for val in range(value+1):
        for coin in coins:
            if coin <= val:
                dp[val] = min(dp[val], dp[val-coin] + 1)
    return dp[value] if dp[value] != float('inf') else -1


if __name__ == '__main__':
    print(coin_change_bottom_up([1,2,5], 5))
    print(coin_change_bottom_up_revision_2([1, 2, 5], 5))