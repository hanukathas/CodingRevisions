def find_pascal_triangle(n: int):
    if n == 1:
        return [[1]]
    mod = int(1e9) + 7
    vals = []
    dp = [[0] * (n) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    result = []

    for i in range(1, n+1):
        vals = []
        for j in range(i):
            dp[i][j] = (dp[i-1][j] + dp[i-1][j-1])%mod
            vals.append(dp[i][j])
        result.append(vals)
    return result

if __name__ == '__main__':
    print(find_pascal_triangle(1700))