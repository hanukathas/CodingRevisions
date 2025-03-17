def zigzag(arr: list):
    for i in range(1, len(arr)):
        if (i-1) % 2 == 0:
            if arr[i-1] >= arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
        elif (i-1) % 2 == 1:
            if arr[i-1] <= arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]

    return arr

if __name__ == '__main__':
    print(zigzag([10,9,8,7,6,5,4,3,2,1]))

