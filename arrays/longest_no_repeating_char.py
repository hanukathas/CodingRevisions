def longest_no_repeating_char(arr: str):
    hmap = {}
    max_size = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] in hmap:
            hmap[arr[i]] += 1
        else:
            hmap[arr[i]] = 1
        while j <= i and hmap[arr[i]] > 1:
            hmap[arr[j]] -= 1
            if hmap[arr[j]] == 0:
                hmap.pop(arr[j])
            j += 1
        max_size = max(max_size, i-j+1)

    return max_size

def longest_no_repeating_char_r(arr: str):
    hmap = {}
    max_size = 0
    left = 0
    for i in range(len(arr)):
        if arr[i] not in hmap:
            hmap[arr[i]] = 1
        else:
            hmap[arr[i]] += 1
        while left <= i and hmap[arr[i]] > 1:
            hmap[arr[left]] -= 1
            if hmap[arr[left]] == 0:
                del hmap[arr[left]]
            left += 1

        max_size = max(max_size, i - left + 1)

    return max_size


if __name__ == '__main__':
    print(longest_no_repeating_char("abaabc"))
    print(longest_no_repeating_char_r("abaabc"))