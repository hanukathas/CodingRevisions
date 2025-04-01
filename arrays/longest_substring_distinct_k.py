def longest_substring_distinct_k(arr: str, k: int):
    max_size = 0
    hmap = {}
    left = 0
    for i in range(len(arr)):

        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            hmap[arr[i]] = 1
        print(hmap)
        while left <= i and len(hmap) > k:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                hmap.pop(arr[left])
            left += 1
        max_size = max(max_size, i - left + 1)
    return max_size

def longest_substring_distinct_k_revision(arr: str, k: int):
    max_size = 0
    hmap = {}
    left = 0
    for i in range(len(arr)):
        hmap[arr[i]] = 1 + hmap.get(arr[i], 0)

        while hmap[arr[i]] > k:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                hmap.pop(arr[left])
            left += 1

        max_size = max(max_size, i - left + 1)

    return max_size

def longest_substring_all_distinct(arr: str):
    max_len = 0
    hmap = {}
    left = 0
    for i in range(len(arr)):
        hmap[arr[i]] = 1 + hmap.get(arr[i], 0)
        while left <= i and hmap[arr[i]] > 1:
            if arr[left] in hmap:
                hmap[arr[left]] -= 1
                if hmap[arr[left]] == 0:
                    hmap.pop(arr[left])
            left += 1

        max_len = max(max_len, i - left + 1)

    return max_len



if __name__ == '__main__':
    # print(longest_substring_distinct_k('efc', 0))
    # print(longest_substring_distinct_k_revision('eefc', 2))
    print(longest_substring_all_distinct('ddddefcccc'))