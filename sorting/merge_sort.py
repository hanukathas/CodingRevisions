def merge_sort(arr):
    """
    Implementation of the merge sort algorithm

    Args:
        arr: List to be sorted

    Returns:
        Sorted list
    """
    # Base case: if array has 1 or fewer elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Divide array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists into a single sorted list

    Args:
        left: First sorted list
        right: Second sorted list

    Returns:
        Merged sorted list
    """
    result = []
    left_index = 0
    right_index = 0

    # Compare elements from both arrays and add smaller one to result
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements
    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def merge_sort_revision(arr: [])-> list:
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_merge = merge_sort_revision(left)
        right_merge = merge_sort_revision(right)

        return merge_revision(left_merge, right_merge)

def merge_revision(left: [], right:[]) -> list:
    i = j = 0
    result = list()
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result



# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort_revision(arr)
    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")