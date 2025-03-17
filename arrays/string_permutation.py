def string_permutation(str1: str, str2: str):
    hmap_str1 = {}
    hmap_str2 = {}
    for i in range(len(str1)):
        if str1[i] in hmap_str1:
            hmap_str1[str1[i]] += 1
        else:
            hmap_str1[str1[i]] = 1

    for i in range(len(str1)):
        if i in hmap_str2:
            hmap_str2[str2[i]] += 1
        else:
            hmap_str2[str2[i]] = 1
    k = len(str1)

    if hmap_str2 == hmap_str1:
        return True

    for i in range(k, len(str2)):

        if str2[i - k] in hmap_str2:
            hmap_str2[str2[i - k]] -= 1
            if hmap_str2[str2[i - k]] == 0:
                hmap_str2.pop(str2[i - k])

        if str2[i] in hmap_str2:
            hmap_str2[str2[i]] += 1
        else:
            hmap_str2[str2[i]] = 1
        print(hmap_str1, hmap_str2)
        if hmap_str2 == hmap_str1:
            return True

    return False

if __name__ == '__main__':
    print(string_permutation("ll", "hello"))
