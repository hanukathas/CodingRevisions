def max_sub_array(arr: list):
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_sum = dp[0]
    for i in range(1, len(arr)):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
        max_sum = max(max_sum, dp[i])
    return max_sum

def max_sub_array_r(arr: list):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    max_sum = 0
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] + arr[i])
        max_sum = max(max_sum, dp[i])

    return max_sum


if __name__ == '__main__':
    print(max_sub_array_r([2,-1,3,4,-5,0]))



