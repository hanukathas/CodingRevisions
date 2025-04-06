def house_robber(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[1], nums[0])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])

    return dp[-1]

def circular_house_robber(arr):
    print(arr[1:-1])
    rob_first_house = house_robber(arr[1:-1])
    print(f"rob_first_house: {rob_first_house}")
    print(arr[:-2])
    dont_rob_first_house = house_robber(arr[:-2])
    print(f"dont_rob_first_house: {dont_rob_first_house}")
    return max(rob_first_house, dont_rob_first_house)


if __name__ == '__main__':
    # print(house_robber([2,10,12,1]))
    # print(house_robber([2, 10, 12, 1, 2]))
    print(circular_house_robber([2, 10, 12, 1, 2]))


