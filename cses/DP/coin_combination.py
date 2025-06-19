def coin_combination2(n: int, x: list):
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in x:
        for i in range(1, n + 1):
            if i >= coin:
                dp[i] = dp[i] + dp[i - coin]

    return dp

def coin_combination1(n: int, x: list):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for coin in x:
            if i >= coin:
                dp[i] = dp[i] + dp[i - coin]

    return dp


if __name__ == '__main__':
    n = 9
    x = [2, 3, 5]
    print(coin_combination1(n, x))