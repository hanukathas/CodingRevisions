def fibonacci(n):
    dp = [0 for i in range(3)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = dp[1] + dp[0]
    for i in range(3, n+1):
        dp[i%3] = dp[(i-1)%3] + dp[(i-2)%3]
    return dp[n%3]
if __name__ == '__main__':
    print(fibonacci(4))
