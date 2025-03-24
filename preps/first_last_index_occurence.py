import heapq


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

def first_last_index_revision(arr: list, target: int):


    def get_index(is_get_low):

        left = 0
        right = len(arr) - 1
        val = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left += 1
            elif arr[mid] > target:
                right -= 1
            else:
                val = mid
                if is_get_low:
                    right = mid -1
                else:
                    left = mid + 1
        return val


    low = get_index(True)
    high = get_index(False)
    return [low, high]



if __name__ == '__main__':
    print(first_last_index([1,2,3,3,5,6,7,7,9,10], 7))
    print(first_last_index_revision([1, 2, 3, 3, 5, 6, 7, 7, 9, 10], 7))