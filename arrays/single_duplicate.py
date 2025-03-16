def single_duplicate(arr: list):
    for i in range(0,len(arr)):
        while arr[i] != i+1:
            d = arr[i] -1
            if arr[d] != arr[i]:
                arr[d], arr[i] = arr[i], arr[d]
            else:
                break

    print(arr[len(arr)-1])
if __name__ == '__main__':
    single_duplicate([1,2,2,3])