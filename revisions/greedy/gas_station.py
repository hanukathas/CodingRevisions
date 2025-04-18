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


if __name__ == '__main__':
    print(gas_station([1,2,3,4,5], [3,4,5,1,2]))

    print(Counter("aabbb"))