def subarray_k_non_repeated_chars(s: str, k: int) -> int:
    hmap = {}
    total = 0
    if len(s) < k:
        return 0

    for i in range(k):
        if s[i] in hmap:
            hmap[s[i]] += 1
        else:
            hmap[s[i]] = 1
    if len(hmap) == k:
        total += 1

    for i in range(k, len(s)):
        if s[i] in hmap:
            hmap[s[i]] += 1
        else:
            hmap[s[i]] = 1

        hmap[s[i-k]] -= 1
        if hmap[s[i-k]] == 0:
            hmap.pop(s[i-k])

        if len(hmap) == k:
            total += 1
    return total

if __name__ == '__main__':
    print(subarray_k_non_repeated_chars("home", 4))



