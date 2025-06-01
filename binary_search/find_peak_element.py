def find_peak_element(arr: list):
    """
    https://leetcode.com/problems/find-peak-element/description/
    :param arr:
    :return:
    """
    start = 1
    end = len(arr) - 2
    while start <= end:
        mid = start + (end - start) // 2
        if arr[start] < arr[mid] > arr[end]: # we found a peak
            return mid
        if arr[start] > arr[mid] < arr[end]:
            start = mid + 1
            end = mid - 1
        if arr[start] < arr[mid] < arr[end]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def test_find_peak_element():
    arr = [1, 3, 20, 4, 1, 0]
    idx = find_peak_element(arr)
    assert 0 <= idx < len(arr), "Index out of bounds"
    left = arr[idx - 1] if idx - 1 >= 0 else float('-inf')
    right = arr[idx + 1] if idx + 1 < len(arr) else float('-inf')
    assert arr[idx] >= left and arr[idx] >= right, "Not a peak"
    print("Test passed.")

test_find_peak_element()

