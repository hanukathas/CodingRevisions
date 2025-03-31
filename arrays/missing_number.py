def missing_number(arr: list):
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[i] in range(len(arr)):
                d = arr[i]
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break

    for i in range(len(arr)):
        if i != arr[i]:
            return i
    return -1

def missing_number_revision(arr: list):
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[i] in range(len(arr)):
                d = arr[i]
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break
    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return -1



if __name__ == '__main__':
    print(missing_number_revision([5,2,1,3]))
    print(missing_number([5, 0, 1, 3]))