import queue
from collections import deque
from queue import SimpleQueue


def subarray_divisible_k(arr, k):
    prefix_sum = 0
    hmap = {0:1}
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

def subarray_divisible_k_revision(arr, k):
    reminder = 0
    prefix_sum = 0
    hmap = {0:1}
    total = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        reminder = prefix_sum % k
        if reminder in hmap:
            total += hmap[reminder]
        if reminder in hmap:
            hmap[reminder] += 1
        else:
            hmap[reminder] = 1
    return total

def subarray_divisible_k_revision_k(arr, k):
    hmap = {0: 1}
    prefix = 0
    total = 0
    for i in range(len(arr)):
        prefix += arr[i]
        reminder = prefix % k

        if reminder in hmap:
            total += hmap[reminder]
        if reminder in hmap:
            hmap[reminder] += 1
        else:
            hmap[reminder] = 1
    return total



if __name__ == '__main__':
    print(subarray_divisible_k([4,5,0,-2,-3,1], 5))
    print(subarray_divisible_k_revision_k([5, 4, 1], 5))
    print(subarray_divisible_k_revision([4, 5, 0, -2, -3, 1], 5))







