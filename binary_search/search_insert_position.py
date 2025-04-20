def search_insert_position(arr: list, n: int):
    start = 0
    end = len(arr) -1

    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == n:
            return mid
        if arr[mid] > n:
            end = mid - 1
        if arr[mid] < n:
            start = mid + 1
    return start

if __name__ == '__main__':
    print(search_insert_position([1,4,5,7,9], 7))
    print(search_insert_position([1, 4, 5, 9], 7))