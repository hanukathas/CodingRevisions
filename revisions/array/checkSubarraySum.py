def checkSubarraySum(nums: list, k: int):
    if len(nums) <= 2:
        return False
    prefix_sum = 0
    hmap = {0: -1} # this is required if the prefix sum % k = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        reminder = prefix_sum % k
        if reminder not in hmap:
            hmap[reminder] = i
        if reminder in hmap:
            if i - hmap[reminder] >= 2:
                return True
    return False


if __name__ == '__main__':
    print(checkSubarraySum([23, 2, 4, 6, 7], 6))
    print(checkSubarraySum([23, 2, 4, 6, 6], 7))
