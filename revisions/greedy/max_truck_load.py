def max_truck_load(box_types: list, truck_size: int):
    box_types.sort(reverse=True, key=lambda item:item[1])
    total_units = 0
    for box_size, box_units in box_types:
        units = min(truck_size, box_size)
        truck_size -= units
        total_units += units * box_units
    return total_units

def max_truck_load_r(box_types: list, truck_size: int):
    box_types_sorted_desc = sorted(box_types, key= lambda items: -items[1])
    print(box_types_sorted_desc)
    load = 0
    for i in range(len(box_types_sorted_desc)):
        load += min(box_types_sorted_desc[i][0], truck_size) * box_types_sorted_desc[i][1]
        truck_size -= min(box_types_sorted_desc[i][0], truck_size)

    return load


if __name__ == '__main__':
    print(max_truck_load([[5,10],[2,5],[4,7],[3,9]], 10))
    print(max_truck_load([[1,3],[2,2],[3,1]], 4))

    print(max_truck_load_r([[5,10],[2,5],[4,7],[3,9]], 10))
    print(max_truck_load_r([[1,3],[2,2],[3,1]], 4))
