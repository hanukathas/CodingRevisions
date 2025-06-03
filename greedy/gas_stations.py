def gas_stations_r(gas: list, cost: list):
    total_tank = 0
    curr_tank = 0
    start = 0
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
    if total_tank < 0:
        return -1
    else:
        return start

def gas_stations(gas: list, cost: list):
    net_travel = 0
    cur_segment = 0
    start_from = 0

    if len(gas) != len(cost):
        return -1

    for station in range(len(gas)):
        net_travel += gas[station] - cost[station]
        cur_segment += gas[station] - cost[station]
        if cur_segment < 0:
            start_from = (station + 1) % len(gas)
            cur_segment = 0
    if net_travel < 0:
        return -1
    else:
        return start_from


if __name__ == "__main__":
    # Test case 1: Possible to complete circuit
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    print(gas_stations(gas, cost))  # Expected: 3

    # Test case 2: Not possible to complete circuit
    gas = [2,3,4]
    cost = [3,4,3]
    print(gas_stations(gas, cost))  # Expected: -1

    # Test case 3: All stations have enough gas
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(gas_stations(gas, cost))  # Expected: 4

    # Test case 4: Only one station
    gas = [5]
    cost = [4]
    print(gas_stations(gas, cost))  # Expected: 0

    # Test case 5: Empty input
    gas = []
    cost = []
    print(gas_stations(gas, cost))  # Expected: 0 or -1 depending on interpretation

