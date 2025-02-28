test1 = [3,1,9,5,11,7,3]
test2 = [1,3,5,7]
test3 = [1,1,1,1]
test4 = [7,3,2,1]
test5 = [5, 8, 3, 9, 4, 1, 7]


def quick_sort(arr, low, high):
    """
    Implementation of quicksort using Hoare's partition scheme

    Args:
        arr: Array to be sorted
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition the array and get the pivot position
        pivot_index = hoare_partition(arr, low, high)

        # Recursively sort the sub-arrays
        quick_sort(arr, low, pivot_index)  # Left sub-array
        quick_sort(arr, pivot_index + 1, high)  # Right sub-array

    return arr


def hoare_partition(arr, low, high):
    """
    Hoare's partition scheme.

    Args:
        arr: Array to be partitioned
        low: Starting index
        high: Ending index

    Returns:
        Partition index
    """
    pivot = arr[low + (high - low) // 2]  # Middle element as pivot
    i = low - 1  # Left pointer
    j = high + 1  # Right pointer

    while True:
        # Move left pointer to the right until it finds an element >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move right pointer to the left until it finds an element <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers crossed, return
        if i >= j:
            return j

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]



if __name__ == '__main__':
    print(quick_sort(test5, 0, high=len(test5) - 1))
    # print(bubble_sort([]))
    # print(bubble_sort(test1))
    # print(bubble_sort(test2))
    # print(bubble_sort(test3))
    # print(bubble_sort(test4))