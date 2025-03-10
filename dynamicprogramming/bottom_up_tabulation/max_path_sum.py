def max_path_sum(grid: list):
    n = len(grid)
    m = len(grid[0])

    dp =[[0] * m for _ in range(n)]

    dp[0][0] = grid[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1,m):
        dp[0][i] = dp[0][i-1] + grid[0][i]

    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = max(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j] )

    return dp[n - 1][m - 1]
if __name__ == '__main__':
    grid = [[1, -4, 3], [4, -2, 2]]
    max_path_sum(grid)
