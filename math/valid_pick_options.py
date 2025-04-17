def valid_pick_options(n: int):
    """
    for a value of n, there are 2n operations.
    for a given order delivery, there are therefore 2n - 1 options
    for the second order, there are therefore 2n -2 options.
    Summing it up, for all delivery orders: Summation of 2n-1 ..... 1
    S = ∑2n-1 = n*(2n-1)
    so from a DP perspective, for f(i), for the delivery of the ith order, the function
    is the total options for f(i-1)th * i*(2i-1).
    :param n:
    :return:
    """
    # base case
    dp = [0] * (n+1)

    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] * i * (2*i - 1)

    return dp[n]


