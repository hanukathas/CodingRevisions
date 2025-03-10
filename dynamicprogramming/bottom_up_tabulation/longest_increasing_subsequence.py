test1 = [10, 9, 2, 5, 3, 7, 101, 18, 195, 6, 1]

def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

if __name__ == '__main__':
    print(longest_increasing_subsequence(test1))