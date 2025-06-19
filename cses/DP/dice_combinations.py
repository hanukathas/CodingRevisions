MOD = 10**9 + 7
def dice_combinations(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                dp[i] = (dp[i] + dp[i-j]) % MOD
    return dp[n]

if __name__ == '__main__':
    n = int(input())
    print(dice_combinations(n))

