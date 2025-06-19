def counting_towers(n):
    MOD = 10**9 + 7
    # dp[i][0]: ways to build i-height tower with separated top blocks
    # dp[i][1]: ways to build i-height tower with connected top block
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1] = [1, 1]  # Base case

    for i in range(2, n + 1):
        # For separated blocks on top:
        # - Add two blocks separately (dp[i-1][0])
        # - Extend previous separated blocks (dp[i-1][0])
        # - Add two blocks on previous full block (dp[i-1][1])
        dp[i][0] = (dp[i-1][0] * 4 + dp[i-1][1]) % MOD

        # For full block on top:
        # - Extend previous full block (dp[i-1][1])
        # - Add full block on separated blocks (dp[i-1][0])
        dp[i][1] = (dp[i-1][0] + dp[i-1][1] * 2) % MOD

    return (dp[n][0] + dp[n][1]) % MOD

if __name__ == '__main__':
    print(counting_towers(6))