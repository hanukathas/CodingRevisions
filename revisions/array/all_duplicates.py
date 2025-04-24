def all_duplicates(arr: list):
    for i in range(len(arr)):
        if arr[i] != i + 1:
            while arr[i] != i + 1:
                d = arr[i] - 1
                if arr[d] != arr[i]:
                    arr[i], arr[d] = arr[d], arr[i]
                else:
                    break
    duplicates = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            duplicates.append(arr[i])

    return duplicates

if __name__ == '__main__':
    print(all_duplicates([1,2,4,3,4]))