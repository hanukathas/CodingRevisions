def first_missing_positive_r(arr: list):
    """
        run the loop  for only positive numbers and break otherwise
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        while arr[i] != i + 1:
            if 0 < arr[i]:
                d = arr[i] - 1
                if arr[d] != arr[i]:
                    arr[i], arr[d] = arr[d], arr[i]
                else:
                    break
            else:
                break

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            return i + 1

if __name__ == '__main__':
    print(first_missing_positive_r([-1, 1,2,3]))
    print(first_missing_positive_r([-11, 2, 0]))