def valid_mountain(arr: list):
    if len(arr) <= 2:
        return False

    for i in range(len(arr) - 1):
        if not arr[i] <= arr[i + 1]:
            break

    for j in range(len(arr)-1, 0, -1):
        if not arr[j] <= arr[j - 1]:
            break

    if i != j:
        return False
    return True

