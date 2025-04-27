from collections import Counter

from greedy.gas_stations import gas_stations


def gas_station(gas: list, cost: list):
    mileage = 0
    min_cost = 0
    gas_station = 0
    for i in range(len(gas)):
        min_cost += gas[i] - cost[i]
        if min_cost < mileage:
            mileage = min_cost
            gas_station = (i + 1) % len(gas) # start from the next one, because this screws things up
    if min_cost < 0:
        return -1
    else:
        return gas_station

def gas_station_r(gas: list, cost: list):
    """
    https://leetcode.com/problems/gas-station/description/
    :param gas:
    :param cost:
    :return:
    """
    running_sum = 0
    min_val = 0
    starting_point = 0

    for i in range(len(gas)):
        running_sum += gas[i] - cost[i]
        if running_sum < min_val:
            starting_point = (i + 1) % len(gas)
            min_val = running_sum
    if running_sum < 0:
        return -1
    else:
        return starting_point



if __name__ == '__main__':
    print(gas_station([1,2,3,4,5], [3,4,5,1,2]))
    print(gas_station_r([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))

