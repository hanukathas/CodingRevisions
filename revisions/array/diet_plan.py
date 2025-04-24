def diet_plan(arr:list, size: int, upper: int, lower: int):
    prefix = sum(arr[:size])
    net = 0
    if prefix < lower:
        net -= 1
    else:
        net += 1


    for i in range(size, len(arr)):
        prefix = prefix + arr[i] - arr[i - size]
        if prefix < lower:
            net -= 1
        else:
            net += 1

    return net


if __name__ == '__main__':
    print(diet_plan([6,5,0,0], 2, 4, 4))
