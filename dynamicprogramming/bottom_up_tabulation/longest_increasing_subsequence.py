test1 = [10, 9, 2, 5, 3, 7, 101, 18, 195, 6, 1]

def longest_increasing_subsequence(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def longest_increasing_subsequence_revision(arr):
    dp = [1] * len(arr)

    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def longest_increasing_subsequence_revision_2(arr):
    """
    define the dp table
    define the base case
    :param arr:
    :return:
    """
    dp = [1] * len(arr)
    n = len(arr)
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    print(longest_increasing_subsequence(test1))
    print(longest_increasing_subsequence_revision_2(test1))