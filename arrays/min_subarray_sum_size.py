def min_subarray_sum_size(arr: list, s: int):
    running_sum = 0
    min_size = float('inf')
    counts = 0
    left = 0
    for i in range(len(arr)):
        print(f"i:{i,arr[i]}")
        running_sum += arr[i]
        while left <= i and running_sum >= s:
            print(arr[left])
            running_sum -= arr[left]
            min_size = min(min_size, i-left+1)
            counts += 1
            left += 1
    print(f"counts: {counts}")
    return min_size

def min_subarray_sum_size_revision(arr: list, s: int):
    min_length = float('inf')
    running_sum = 0
    left = 0
    count = 0
    for i in range(len(arr)):
        running_sum += arr[i]
        while left <= i and running_sum >= s:
            running_sum -= arr[left]
            min_length = min(min_length, i - left + 1)
            left += 1
            count += 1
    return min_length, count

# only correct solution
def min_subarray_sum_size_revision_2(arr: list, s: int):
    prefix_sum = 0
    left = 0
    min_length = float('inf')
    count = 0

    for i in range(len(arr)):
        prefix_sum += arr[i]
        while left<=i and prefix_sum > s:
            prefix_sum -= arr[left]
            left += 1
        if prefix_sum == s:
            min_length = min(min_length, i - left + 1)

    return min_length

if __name__ == '__main__':
    # print(min_subarray_sum_size([4,8,2,6,1,5,11], 10))
    print(min_subarray_sum_size_revision([2,3,1,2,4,3], 8))
    print(min_subarray_sum_size_revision_2([2, 3, 1, 2, 4, 3], 8))

