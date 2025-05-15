import heapq
from typing import List


def car_pooling(trips: list, capacity: int):
    passengers = [0] * 1001 # from to range is 0 to 1000
    for trip in trips:
        passengers[trip[1]] += trip[0]
        passengers[trip[2]] -= trip[0]
    print(passengers)
    current_passengers = 0
    for passenger in passengers:
        current_passengers += passenger
        if current_passengers > capacity:
            return False
    return True


def carPooling(trips: List[List[int]], capacity: int) -> bool:
    # Create a timeline array of size 1001 (given constraint)
    timeline = [0] * 1001

    # Add passengers at pickup and remove at dropoff
    for passengers, start, end in trips:
        timeline[start] += passengers  # Add passengers at pickup
        timeline[end] -= passengers  # Remove passengers at dropoff

    # Track current passengers using prefix sum
    current_passengers = 0
    for passengers in timeline:
        current_passengers += passengers
        if current_passengers > capacity:
            return False

    return True


if __name__ == '__main__':
    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    print(car_pooling(trips, capacity))
    print(carPooling(trips, capacity))

