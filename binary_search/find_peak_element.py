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



