def search_rotated_sorted_array(nums: list, target: int):
    start = 0
    end = len(nums) - 1

    region = ""

    if nums[-1] > target:
        region = "brown"
    elif nums[-1] < target:
        region = "green"
    else:
        return len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        print(start, end, mid)
        if nums[mid] == target:
            return mid
        elif nums[mid] < nums[-1] and region == 'green':
            start = mid + 1
        elif nums[-1] < nums[mid] and region == 'brown':
            start = mid + 1
        elif nums[-1] < nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1

    return -1


if __name__ == '__main__':
    print(search_rotated_sorted_array([6, 7, 8, 0, 1, 2], 8))
