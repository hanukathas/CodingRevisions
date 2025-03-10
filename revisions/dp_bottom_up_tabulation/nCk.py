def nCk(n:int, r:int):
    dp = [[0] * (r+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, min(i+1,r+1)): #take min because 1C2 is not defined
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp
if __name__ == '__main__':
    print(nCk(4,2))