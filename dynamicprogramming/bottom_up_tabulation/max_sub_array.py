def max_subarray(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], arr[i] + dp[i - 1])
        max_sum = max(max_sum, dp[i])

    return max_sum


def max_subarray_bottom_up(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1, n):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


if __name__ == '__main__':
    print(max_subarray_bottom_up([1, 2, 3, -4, 5, 6, 7]))
    print(max_subarray([1, 2, 3, -4, 5, 6, 7]))
