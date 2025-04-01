def max_erasure_val(nums: list) -> int:
    running_sum = 0
    max_sum = 0
    left = 0
    seen = set()
    for i in range(len(nums)):
        while nums[i] in seen:
            seen.remove(nums[i])
            left += 1
            running_sum -= nums[i]
        seen.add(nums[i])
        running_sum += nums[i]

        max_sum = max(max_sum, running_sum)

    return max_sum
if __name__ == '__main__':
    print(max_erasure_val([4,2,4,5,6]))
    print(max_erasure_val([5,2,1,2,5,2,1,2,5]))