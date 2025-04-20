def array_reader(index: int):
    arr = [-5,-4,-3,-2,-1,0]
    if index <= len(arr) -1:

        return arr[index]
    else:
        return -1

def search_unknown_size_array(target: int):
    """
    problem: I don't know the size of the array, so I do not know start and end
    to find the position of target, we go log2N so continuously divide the size of array by n
    step 1: check if target is the 1st element
    step 2: starting at end = 1 (then start becomes 0), see if the target is less than or greater than
    step 3: when target is less than arr[end] then arr[end/2] < number < arr[end]

    :param target:
    :return:
    """
    if array_reader(0) == target:
        return 0
    end = 1
    go = True
    while go:
        if array_reader(end) >= target or array_reader(end) == -1:
            go = False
        if not go:
            break
        end *= 2

    if array_reader(end) == target:
        return end
    start = end // 2

    while start <= end:
        mid = start + (end - start) // 2
        if array_reader(mid) == target:
            return mid
        elif array_reader(mid) < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


if __name__ == '__main__':
    print(search_unknown_size_array(9))
    print(search_unknown_size_array(5))
    print(search_unknown_size_array(100))
    print(search_unknown_size_array(-1))
    print(search_unknown_size_array(-5))
