def minimum_coins(coins, value):
    dp = [float('inf')] * (value+1)
    dp[0] = 0
    for i in range(value+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[value] if dp[value] != float('inf') else -1

 
if __name__ == '__main__':
    print(minimum_coins([2,3,5], 10))