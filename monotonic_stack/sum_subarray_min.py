def sum_subarray_min(arr: list):
    total_sum = 0
    dp = [0] * len(arr)
    subarray_min_stack = []

    for i in range(len(arr)):
        while subarray_min_stack and subarray_min_stack[-1][0] > arr[i]:
            subarray_min_stack.pop()
        if subarray_min_stack:
            span = i - subarray_min_stack[-1][1]
            dp[i] = dp[subarray_min_stack[-1][1]]
        else:
            span = i + 1

        dp[i] += span * arr[i]

        subarray_min_stack.append((arr[i], i))
        total_sum += dp[i]
        # print(total_sum)

    return total_sum

def sum_subarray_min_r(arr: list):
    min_stack = []
    n = len(arr)
    dp = [0] * n
    total = 0
    for i in range(len(arr)):
        while min_stack and min_stack[-1][0] > arr[i]:
            min_stack.pop()
        if min_stack:
            span = i - min_stack[-1][1]
            dp[i] = dp[min_stack[-1][1]]
        else:
            span = i + 1

        dp[i] += span * arr[i]
        total = total + dp[i]
        min_stack.append([arr[i], i])
    return total


if __name__ == '__main__':
    print(sum_subarray_min([3,1,2,4]))
    print(sum_subarray_min([11,81,94,43,3]))

    print(sum_subarray_min_r([3,1,2,4]))
    print(sum_subarray_min_r([11,81,94,43,3]))

