def min_cost_tickets(days: list, costs: list):
    """
    for a given day, I am going to buy a pass that keeps the cost to
    the minimum
    :param days:
    :param cost:
    :return:
    """
    dp = [0] * len(days)
    dp[0] = min(costs)

    for i in range(1, len(days)):

        case1 = dp[i-1] + costs[0]

        j = i - 1
        while j >= 0 and days[j] >= days[i] - 6:
            j -= 1
            
        case2 = float('inf')

        if j >= 0:
            case2 = dp[j] + costs[1]
        else:
            case2 = costs[1]

        j = i - 1
        while j >= 0 and days[j] >= days[i] - 29:
            j -= 1
        case3 = float('inf')

        if j >= 0:
            case3 = dp[j] + costs[2]
        else:
            case3 = costs[2]


        dp[i] = min(case1, case2, case3)


    return dp[len(days) - 1]


if __name__ == '__main__':
    print(min_cost_tickets([1, 3, 5, 9, 20], [3, 7, 15]))
