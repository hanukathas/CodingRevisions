def climbing_stairs(n):
    dp = {1: 1, 2: 2}
    i = 3
    while i <= n:
        dp[i] = dp[i-1] + dp[i-2]
        i += 1
    return dp[n]


def climb_stairs_bottom_up(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

if __name__ == '__main__':
    print(climbing_stairs(17))
    print(climb_stairs_bottom_up(17))




