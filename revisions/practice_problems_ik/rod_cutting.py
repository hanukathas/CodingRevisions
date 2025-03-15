def rod_cutting(price):
    n = len(price)
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = price[0]
    for i in range(1, n+1):
        max_val = -1
        for j in range(i):

            max_val = max(max_val, price[j]+dp[i-j-1])
        dp[i] = max_val
    return dp[n]

if __name__ == '__main__':
    i = [8, 4, 2]
    print(rod_cutting(i))
