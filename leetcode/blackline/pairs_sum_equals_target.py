def find_pairs(nums, target):
    seen = set()
    result = []
    for num in nums:
        compliment = target - num
        if compliment in seen:
            result.append([compliment, num])
        seen.add(num)

    return result

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = find_pairs(nums, target)
    print(f"Input array: {nums}")
    print(f"Target sum: {target}")
    print(f"Pairs found: {result}")
