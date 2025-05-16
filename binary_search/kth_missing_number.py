def kth_missing_number(nums: list, k: int):
    start = 0
    n = len(nums)
    end = n - 1
    missing = 0
    while start <= end:
        mid = start + (end - start) // 2
        missing = nums[mid] - (nums[0] + mid)
        if missing < k:
            start = mid + 1
        else:
            end = mid - 1

    # print(start, end, missing)
    missing = nums[end] - (nums[0] + end)
    # print(missing)
    return nums[end] + k - missing

def kth_missing_number_r(nums: list, k: int):
    start = 0
    n = len(nums)
    end = n - 1
    missing = 0 # after calculating mid, get how many values are missing
    # missing = nums[mid] - (nums[start] + mid)
    while start <= end:
        mid = start + (end - start) // 2
        missing = nums[mid] - (nums[0] + mid)
        if missing < k:
            start = mid + 1
        else:
            end = mid - 1
    missing = nums[end] - (nums[0] + end)
    return nums[end] + k - missing


if __name__ == '__main__':
    # print(kth_missing_number([4, 7, 9, 10], 1))
    print(kth_missing_number([4, 7, 9, 10], 3))
    print(kth_missing_number_r([4, 7, 9, 10], 3))
