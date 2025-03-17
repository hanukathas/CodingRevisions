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

if __name__ == '__main__':
    print(min_subarray_sum_size([4,8,2,6,1,5,11], 10))

