def sum_subarray_min(arr: list):
    subarray_min_stack = []
    total_sum = 0
    n = len(arr)
    local_ans = [0] * n

    for i in range(n):
        while subarray_min_stack and subarray_min_stack[-1][0] >= arr[i]:
            subarray_min_stack.pop()
        if subarray_min_stack:
            span = i - subarray_min_stack[-1][1]
            local_ans[i] = local_ans[subarray_min_stack[-1][1]]
        else:
            span = i + 1
        local_ans[i] += arr[i] * span
        total_sum += total_sum + local_ans[i]
        subarray_min_stack.append((arr[i], i))
    return  total_sum

if __name__ == '__main__':
    print(sum_subarray_min([3,1,2,4]))




