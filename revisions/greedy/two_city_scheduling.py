def two_city_scheduling(costs: list):
    costs.sort(key=lambda item: abs(item[0] - item[1]))

    print(costs)
    required_n = len(costs) // 2
    num_a = 0
    num_b = 0
    min_costs = 0
    for cost in costs:
        if num_b == required_n:
            num_a += 1
            min_costs += cost[0]
        elif num_a == required_n:
            num_b += 1
            min_costs += cost[1]
        elif cost[0] < cost[1]:
            num_a += 1
            min_costs += cost[0]
        else:
            num_b += 1
            min_costs += cost[1]
    return min_costs


if __name__ == '__main__':
    print(two_city_scheduling([[10, 20], [30, 200], [400, 50], [30, 20]]))
