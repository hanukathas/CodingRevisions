def max_consecutive_1(arr, k):
    max_count = 0
    left = 0
    running_sum = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            running_sum += 1
        while left <= i and running_sum > k:
            if arr[left] == 0:
                running_sum -= 1
            left += 1
        max_count = max(max_count, i - left + 1)
    return max_count


if __name__ == '__main__':
    print(max_consecutive_1([1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1], 2))
