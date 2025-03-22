def min_cost_climbing_stairs(cost: list):
    dp = [0 * i for i in range(len(cost)+2)]
    dp[1] = cost[0]

    cost.append(0)
    for i in range(2, len(dp)):
        dp[i] = cost[i-1] + min(dp[i-1], dp[i-2])
    print(dp[len(cost)])

def min_cost_climbing_stairs_revision(cost: list):
    dp = [0 * i for i in range(len(cost)+2)]
    dp[1] = cost[0]
    cost.append(0)
    for i in range(2, len(dp)):
        dp[i] = cost[i-1] + min(dp[i-1], dp[i-2])
    print(dp[len(cost)])


if __name__ == '__main__':
    min_cost_climbing_stairs([1, 1, 2])
    min_cost_climbing_stairs([3, 4])
    min_cost_climbing_stairs_revision([3, 4])