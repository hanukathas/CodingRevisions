def max_area_container(arr: list):
    max_area = 0
    i = 0
    j = len(arr) - 1
    while i < j:
        area = (j-1) * min(arr[i], arr[j])
        max_area = max(max_area, area)
        if arr[i] <= arr[j]:
            i += 1
        else:
            j -= 1
    return max_area

if __name__ == '__main__':
    print(max_area_container([4,3,20,3,20,10]))