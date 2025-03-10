def unique_paths(n: int, m: int):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp
if __name__ == '__main__':
    print(unique_paths(3,2))