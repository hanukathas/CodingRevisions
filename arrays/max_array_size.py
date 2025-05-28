from sys import prefix


def max_array_size_rmax_array_size(nums: list, k: int) -> int:
    prefix_sum = 0
    hmap = {0: 0}
    global_max = 0
    for i in range(len(nums)):
        prefix_sum += nums[i]
        if prefix_sum - k in hmap:
            global_max = max(global_max, i + 1 - hmap[prefix_sum - k])  # add one to increment count by 1

        # learning: to get the position of the prefix-sum
        if prefix_sum not in hmap:
            hmap[prefix_sum] = i + 1

    return global_max

def max_array_size_r(nums: list, k: int) -> int:
    prefix = 0
    max_size = 0
    hmap = {0: 0} # initialize for empty array
    for i in range(len(nums)):
        prefix += nums[i]

        if prefix - k in hmap:
            print(prefix, nums[i], prefix - k, hmap)
            max_size = max(max_size, i + 1 - hmap[prefix - k])
        if prefix not in hmap:
            hmap[prefix] = i + 1

    return max_size

def max_array_size_r2(nums: list, k: int):
    if len(nums) == 0:
        return 0
    prefix = 0
    max_length = 0
    hmap = {}
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix - k in hmap:
            max_length = max(max_length, i + 1 - hmap[prefix - k])
        if prefix not in hmap:
            hmap[prefix] = i + 1
    return max_length

if __name__ == '__main__':
    # print(max_array_size_rmax_array_size([1, -1, 5, -2, 3], 3))
    # print(max_array_size_rmax_array_size([-2, -1, 2, 1], 1))
    print(max_array_size_r([1, -1, 5, -2, 3], 3))
    # print(max_array_size_r([-2, -1, 2, 1], 1))
