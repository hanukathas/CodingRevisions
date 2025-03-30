import heapq
from ctypes import c_char


def place_n_flowers(arr: list):
    i = 0
    n = 0

    while i < len(arr):

        if arr[i] == 1:
            i += 2
        else:
            if i == 0:
                if arr[1] == 0:
                    arr[0] = 1
                    i = 2
                    n += 1
            elif i == len(arr) - 1 and arr[i] != 1:
                if arr[i - 1] == 0:
                    arr[len(arr) - 1] = 1
                    n += 1
                    break
            elif arr[i-1] == 0 and arr[i+1] == 0:
                arr[i] = 1
                i += 2
                n += 1
            else:
                i += 1
    return n

def first_last_index(arr: list, target: int):
    """
    for first go from mid to end since it's sorted
    for last go from mid to first since it's sorted
    let's use leadership mindset to solve this problem:
    1. divide the array, and see if the mid is target
    """
    def binary_search(find_first: bool):
        left = 0
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                result = mid
                if find_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    first = binary_search(True)
    last = binary_search(False)
    return [first, last]




if __name__ == '__main__':
    print(place_n_flowers([1, 0, 0, 0, 1]))
    print(str(-2))
    print(heapq.nlargest(1, [1, 2, 3, 4, 5])[-1])
