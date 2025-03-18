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

if __name__ == '__main__':
    print(longest_substring_distinct_k('aaabbb', 1))