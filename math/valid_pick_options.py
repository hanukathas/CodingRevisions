def r_valid_pick_options(n: int):
    """
    for one order I can fill it in 1 way -> 2 slots, 1pick and 1drop -> only one way possible
    for two orders, there are 4 slots. I need to fulfill, the first order in 4C2 ways and the last one in 1C1 ways.
    for third order, there is are 6C2 * 4C2 * 1C1. This is a series that yields n(2n-1)
    :param number:
    :return:
    """
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] * i * (2*i - 1)

    return dp[n]

def r_valid_pick_options_r(n: int):
    """
    https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/description/
    :param n:
    :return:
    """
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] * i * (2 * i - 1)
    return dp[n]

if __name__ == '__main__':
    print(r_valid_pick_options(3))
    print(r_valid_pick_options_r(3))