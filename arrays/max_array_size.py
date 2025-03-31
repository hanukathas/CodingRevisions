def max_array_size(nums: list, k: int) -> int:
    prefix_sum = 0
    hmap = {0: 0}
    global_max = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in hmap:
            global_max = max(global_max, i+1 - hmap[prefix_sum - k])

        # learning: to get the position of the prefix-sum
        if prefix_sum not in hmap:
            hmap[prefix_sum] = i + 1

    return global_max
if __name__ == '__main__':
    print(max_array_size([1,-1,5,-2,3], 3))
    print(max_array_size([-2, -1, 2, 1], 1))

