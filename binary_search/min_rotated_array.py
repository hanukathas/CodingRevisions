def min_rotated_array(nums: list):
    start = 0
    end = len(nums) -1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] <= nums[-1]:
            end = mid - 1
        else:
            start = mid + 1
    return nums[start]