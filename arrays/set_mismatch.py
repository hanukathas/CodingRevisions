def set_mismatch(arr: list):
    for i in range(len(arr)):
        while arr[i] != i+1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break

    for i in range(len(arr)):
        if arr[i] != i+1:
            return arr[i], i+1

if __name__ == '__main__':
    print(set_mismatch([1,2,2,4]))