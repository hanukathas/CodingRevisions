def climbing_stairs(n):
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return  dp[n]

def climbing_stairs_r(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == '__main__':
    print(climbing_stairs(3))
    print(climbing_stairs_r(4))