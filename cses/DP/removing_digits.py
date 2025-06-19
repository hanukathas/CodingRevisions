def removing_digits(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for d in str(n):
            dp[i] = min(dp[i], dp[i - int(d)] + 1)
    print(dp)
    return dp[n]


if __name__ == '__main__':
    print(removing_digits(27))