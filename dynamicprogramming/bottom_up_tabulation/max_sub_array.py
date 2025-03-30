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

def max_subarray_bottom_up_revision(arr):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]
    for i in range(len(arr)):
        dp[i] = max(arr[i], dp[i-1]+arr[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

def max_subarray_bottom_up_revision_2(arr):
    """
        logic: current number i.e. starts from the current number
        or the sum from previous, whichever gives the max value
        keep the max array because the last few elements could be all -ve

        if the array size is 1, return the array. no elements then 0

        dp table, will be a single dimensional with len(arr) + 1 elements
    :param arr:
    :return:
    """
    dp = [0] * (len(arr))
    dp[0] = arr[0]
    max_sum = dp[0]

    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
        max_sum = max(max_sum, dp[i])
    return max_sum






if __name__ == '__main__':
    print(max_subarray_bottom_up([1, 2, 3, -4, 5, 6, 7]))
    print(max_subarray([1, 2, 3, -4, 5, 6, 7]))
    print(max_subarray_bottom_up_revision_2([1, 2, 3, -4, 5, 6, 7]))
