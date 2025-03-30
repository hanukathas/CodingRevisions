def unique_paths(n, m):
    # Create dp table
    mod = int(1e9) + 7
    dp = [[0] * m for _ in range(n)]

    # Initialize first row and column
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1

    # Fill dp table
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

    return dp[n - 1][m - 1]

def unique_paths_revision(n, m):
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1

    for j in range(m):
        dp[0][j] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

if __name__ == '__main__':
    print(unique_paths(3,2))
    print(unique_paths_revision(3, 2))

