def decode_ways(s: str):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1 # base case
    dp[1] = 1

    for i in range(2, len(s) + 1):
        print(dp)
        if s[i-1] != '0':
            dp[i] = dp[i-1]

        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[n]

if __name__ == "__main__":
    print(decode_ways("12114"))