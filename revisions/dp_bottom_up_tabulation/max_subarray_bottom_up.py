def max_subarray_bottom_up(arr: list):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1]+arr[i])
        max_sum = max(dp[i], max_sum)
    return max_sum
if __name__ == '__main__':
    print(max_subarray_bottom_up([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
