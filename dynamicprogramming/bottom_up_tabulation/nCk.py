def nCk(n: int,r: int):
    p = 10e9+7
    if r > n:
        return 0
    dp = [[0 for _ in range(r + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    print(dp)
    for i in range(1, n+1):
        for j in range(1, min(i+1,r+1)):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1] % p
    print(dp)
    return dp[n][r]

if __name__ == '__main__':
    print(nCk(5,3))

