def r_maximal_score_good_subarray(nums: list, k: int):
    n = len(nums)
    left_span = [0] * n
    right_span = [0] * n
    subarray_stack = []
    for i in range(n):
        while subarray_stack and subarray_stack[-1][0] >= nums[i]:
            subarray_stack.pop()

        if subarray_stack:
            left_span[i] = i - subarray_stack[-1][1]
        else:
            left_span[i] = i + 1
        subarray_stack.append((nums[i], i))

    subarray_stack = []

    for i in range(n-1, -1, -1):
        while subarray_stack and subarray_stack[-1][0] >= nums[i]:
            subarray_stack.pop()
        if subarray_stack:
            right_span[i] = subarray_stack[-1][1] - i
        else:
            right_span[i] = n - i
        subarray_stack.append((nums[i], i))

    max_subarray_score = 0

    for i in range(len(nums)):
        if i - left_span[i] + 1 <= k <= i + right_span[i] - 1:
            max_subarray_score = max(max_subarray_score, ((left_span[i] + right_span[i] - 1)* nums[i]))

    return max_subarray_score

if __name__ == '__main__':
    print(r_maximal_score_good_subarray([1,4,3,7,4,5], 3))


