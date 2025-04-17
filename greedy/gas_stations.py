def gas_stations(gas:list, cost:list):
    """
        1. start from the place where gas - cost is minimum.
        2. 1 gives the worst case scenario
    :param gas:
    :param cost:
    :return:
    """
    to_start = 0
    min_val = gas[0] - cost[0]
    running_sum = 0
    for i in range(1, len(gas)):
        running_sum += gas[i] - cost[i]
        if min_val < gas[i] - cost[i]:
            to_start = (i + 1) % len(gas)
            min_val = gas[i] - cost[i]

    if running_sum < 0:
        return -1
    else:
        return to_start


