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

def nCk_revision(n: int,k: int):
    mod = int(1e9)+7
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1 #nC0 is 1
    for i in range(1, n+1):
        for j in range(1, min(i+1, k+1)):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]



if __name__ == '__main__':
    print(nCk(5,3))
    print(nCk_revision(5, 3))

