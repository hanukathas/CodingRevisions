
def single_element(arr: list, target: int):
    """
    here, we need to understand that if the value > index and target is less than that value, then
    the target and index cannot be same.
    but an index can store a value less than the index
    so the catch is this: middle element can have a value <= mid
    :param arr:
    :param target:
    :return:
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    if start == len(arr) or start != arr[start]:
        return -1
    else:
        return start


if __name__ == '__main__':
    print(single_element([-1,0,1,3,5], 3))

