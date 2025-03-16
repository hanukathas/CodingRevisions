def missing_number(arr: list):
    for i in range(len(arr)):
        while arr[i] != i:
            if arr[i] in range(len(arr)):
                d = arr[i]
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break
    print(arr)
    for i in range(len(arr)):
        if i != arr[i]:
            return i
    return -1

if __name__ == '__main__':
    print(missing_number([3,0,1,2]))