def maximum_stolen_value(values):
    dp = [0] * (len(values)+1)
    dp[0] = 0
    dp[1] = values[0]
    print(dp)
    for i in range(1, len(values)):
        dp[i+1] = max(values[i]+dp[i-1], dp[i])
    return dp[len(values)]




if __name__ == '__main__':
    print(maximum_stolen_value([7, 9, 9, 6, 4, 3, 8, 9, 5, 3, 3, 5]))