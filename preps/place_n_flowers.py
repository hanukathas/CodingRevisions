def place_n_flowers(arr: list):
    i = 0
    n = 0

    while i < len(arr):

        if arr[i] == 1:
            i += 2
        else:
            if i == 0:
                if arr[1] == 0:
                    arr[0] = 1
                    i = 2
                    n += 1
            elif i == len(arr) - 1 and arr[i] != 1:
                if arr[i - 1] == 0:
                    arr[len(arr) - 1] = 1
                    n += 1
                    break
            elif arr[i-1] == 0 and arr[i+1] == 0:
                arr[i] = 1
                i += 2
                n += 1
            else:
                i += 1
    return n






if __name__ == '__main__':
    print(place_n_flowers([1, 0, 0, 0, 1]))
