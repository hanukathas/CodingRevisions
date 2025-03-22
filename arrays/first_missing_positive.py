def first_missing_positive(arr: list):
    for i in range(len(arr)):
        while arr[i] != i+1:
            if 0 < arr[i] <= len(arr):
                d = arr[i] -1
                if arr[d] != arr[i]:
                    arr[i], arr[d] = arr[d], arr[i]
                else:
                    break
            else:
                break
        print(arr[i], arr)
        if arr[i] > 0 and arr[i] != i+1:
            return i+1
    for i in range(len(arr)):
        if i+1 != arr[i]:
            return i+1


if __name__ == '__main__':
    print(first_missing_positive([3,5,-1,1]))
    print()