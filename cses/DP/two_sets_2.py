def two_sets_2(n: int) -> int:
    # If n*(n+1)/2 is odd, it's impossible to divide into equal sums
    total = n * (n + 1) // 2
    if total % 2 != 0:
        return 0

    # Target sum for each subset
    target = total // 2
    MOD = 1_000_000_007

    # dp[i][j] represents number of ways to make sum j using numbers from 1 to i
    dp = [[0] * (target + 1) for _ in range(n + 1)]

    # Base case: empty set can make sum 0
    dp[0][0] = 1

    # For each number from 1 to n
    for i in range(1, n + 1):
        # For each possible sum from 0 to target
        for j in range(target + 1):
            # Don't take number i
            dp[i][j] = dp[i - 1][j]

            # Take number i if possible (sum - i >= 0)
            if j >= i:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - i]) % MOD

    # Return result (divide by 2 as each valid division is counted twice)
    return (dp[n][target] * pow(2, MOD - 2, MOD)) % MOD


def main():
    n = int(input())
    print(two_sets_2(n))


if __name__ == '__main__':
    print(two_sets_2(7))