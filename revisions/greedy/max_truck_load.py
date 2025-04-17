def max_truck_load(box_types: list, truck_size: int):
    box_types.sort(reverse=True, key=lambda item:item[1])
    total_units = 0
    for box_size, box_units in box_types:
        units = min(truck_size, box_size)
        truck_size -= units
        total_units += units * box_units
    return total_units



if __name__ == '__main__':
    print(max_truck_load([[5,10],[2,5],[4,7],[3,9]], 10))
    print(max_truck_load([[1,3],[2,2],[3,1]], 4))
