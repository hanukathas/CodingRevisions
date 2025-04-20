def missing_ap_number(arr: list):
    """
    here we find the missing arithmatic progression number
    so if the len of the elements is greater than 3, then we can find it
    if the len is 3 then the middle element has to be the average
    we know that arithmatic progression is given by a, a+d, a+2d, a+3d
    so the last element = (end - start) / (n - 1)

    :param arr:
    :return:
    """
    if len(arr) <= 2:
        return -1
    if len(arr) == 3:
        if arr[1] != (arr[0] + arr[1]) / 2:
            return arr[1]
        else:
            return -1
    if all(element == arr[0] for element in arr):
        return arr[0]

    d = (arr[-1] - arr[0]) / len(arr)
    start = 0
    end = len(arr) - 1
    # middle = start +
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == arr[0] + mid * d:
            start = mid + 1
        else:
            end = mid - 1

    return arr[end] + d

if __name__ == '__main__':
    print(missing_ap_number([5,7,11,13]))

