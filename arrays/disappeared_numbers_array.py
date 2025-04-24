def disappeared_numbers_array(arr: list):
    for i in range(len(arr)):
        while arr[i] != i+1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[d], arr[i] = arr[i], arr[d]
            else:
                break
    disappeared = []
    for i in   range(len(arr)):
        if arr[i] != i+1:
            disappeared.append(i+1)
    return disappeared

def disappeared_numbers_array_r(arr: list):
    for i in range(len(arr)):
        if arr[i] != i + 1:
            while arr[i] != i + 1:
                b = arr[i] - 1
                if arr[i] != arr[b]:
                    arr[i], arr[b] = arr[b], arr[i]
                else:
                    break
    disappeared = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            disappeared.append(i+1)

    return disappeared



if __name__ == '__main__':
    print(disappeared_numbers_array_r([4, 3, 2, 7, 8, 2, 3, 1]))
