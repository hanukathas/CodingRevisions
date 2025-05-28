def fruits_into_baskets(arr: list):
    max_size = 0
    hmap = {}
    left = 0
    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            hmap[arr[i]] = 1
        while left <= i and len(hmap) > 2:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                hmap.pop(arr[left])
            left += 1
        max_size = max(max_size, i - left + 1)
    return max_size


def fruits_into_baskets_revision(arr: list):
    max_size = 0
    left = 0
    hmap = {}
    for i in range(len(arr)):
        hmap[arr[i]] = 1 + hmap.get(arr[i], 0)
        while len(hmap) > 2:
            if arr[left] in hmap:
                hmap[arr[left]] -= 1
                if hmap[arr[left]] == 0:
                    hmap.pop(arr[left])
            left += 1
        max_size = max(max_size, i - left + 1)
    return max_size


def fruits_into_baskets_r(arr: list):
    hmap = {}
    left = 0
    max_size = 0

    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            hmap[arr[i]] = 1

        while left <= i and len(hmap) > 2:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                del hmap[arr[left]]
            left += 1
        max_size = max(max_size, i - left + 1)
    return max_size




if __name__ == '__main__':
    print(fruits_into_baskets_r([1, 2, 3, 2, 2]))
    print(fruits_into_baskets_r([1, 2, 3, 2, 2]))
