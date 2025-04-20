def single_element_array(arr: list):
    """
    suppose the array is [1,1,2,2,3,4,4,5,5]
    to the left of single element, the two consecutive elements will have odd index followed by even index
    after the single element, the two consecutive elements will have even index followed by odd index

    check if the single element is to the left or right extreme
    :param arr:
    :return:
    """
    n = len(arr)
    if len(arr) == 0:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[-1] != arr[n-2]:
        return arr[n-1]

    start = 0
    end = n - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid - 1] != arr[mid] and arr[mid] != arr[mid + 1]:
            return arr[mid]
        # element is to the left of mid if:
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            start = mid + 1
        else:
            end = mid - 1

    return -1

if __name__ == '__main__':
    print(single_element_array([1,1,2,2,3,4,4,5,5]))


