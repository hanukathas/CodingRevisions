def coin_change_bottom_up(coins: list, value: int):
    dp = [float('inf')] * (value+1)
    dp[0] = 0
    for val in range(1, value+1):
        for coin in coins:
            if coin <= val:
                dp[val] = min(dp[val], dp[val - coin] + 1)

    return dp[value] if dp[value] != float('inf') else -1

if __name__ == '__main__':
    print(coin_change_bottom_up([1,5,10], 72))

