def fruits_into_baskets(arr: list):
    max_size = 0
    hmap = {}
    left = 0
    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            hmap[arr[i]] = 1
        while left <= 1 and len(hmap) > 0:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                hmap.pop(arr[left])
            left += 1
        max_size = max(max_size, i-left + 1)
    return max_size

if __name__ == '__main__':
    print(fruits_into_baskets([0,1,2,2,1,3,0]))

