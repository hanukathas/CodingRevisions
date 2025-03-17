import queue
from collections import deque
from queue import SimpleQueue


def subarray_divisible_k(arr, k):
    prefix_sum = 0
    hmap = {}
    total = 0
    rem = 0
    for num in arr:
        prefix_sum = (prefix_sum + num)
        rem = prefix_sum % k
        if rem in hmap:
            total += hmap[rem]
        if rem not in hmap:
            hmap[rem] = 1
        else:
            hmap[rem] += 1
    return  total

if __name__ == '__main__':
    print(subarray_divisible_k([4, 5, 0, -2, -3, 1], 5))







