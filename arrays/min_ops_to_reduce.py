from arrays.subarray_product_lesser_k import subarray_product_lesser_k


def min_ops_to_reduce(arr: list, k: int):
    min_ops = -1
    reduced_k = sum(arr) - k
    left = 0
    running_sum = 0
    for i in range(len(arr)):
        running_sum += arr[i]
        while left <= i and running_sum > reduced_k:
            running_sum -= arr[left]
            left += 1

        if running_sum == reduced_k:
            min_ops = max(min_ops, i - left + 1)

    return min_ops if min_ops == -1 else len(arr) - min_ops


if __name__ == '__main__':
    print(min_ops_to_reduce([9], 5))
