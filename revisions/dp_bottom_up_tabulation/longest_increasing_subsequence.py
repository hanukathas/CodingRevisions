def longest_increasing_subsequence(arr: list):
    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return dp[-1]

if __name__ == '__main__':
    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))