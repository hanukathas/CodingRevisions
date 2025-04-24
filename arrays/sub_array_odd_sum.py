from sys import prefix


def sub_array_odd_sum(arr: list) -> int:
    """
    total number of odd sum sub arrays
    :param arr:
    :return:
    """
    prefix_sum = 0
    # empty array is even sum, so when we start, event = 1, odd = 0
    hmap = {'even': 1, 'odd': 0}
    total = 0
    for i in range(len(arr)):
        prefix_sum = prefix_sum + arr[i]
        if prefix_sum % 2 == 0:
            total += hmap['odd']
        else:
            total += hmap['even']
        print(hmap, total)
        if prefix_sum % 2 != 0:
            hmap['odd'] += 1
        else:
            hmap['even'] += 1
    return  total

def sub_array_odd_sum_r(arr: list):
    odd_even = {0:1, 1:0}
    total = 0
    prefix = 0

    for i in range(len(arr)):
        prefix += arr[i]
        if prefix % 2 == 0:
            total += odd_even[1]
        else:
            total += odd_even[0]

        if prefix % 2 == 0:
            odd_even[0] += 1
        else:
            odd_even[1] += 1

    return total

if __name__ == '__main__':
    print(sub_array_odd_sum([1,3,5]))
    print(sub_array_odd_sum_r([1, 3, 5, 79]))