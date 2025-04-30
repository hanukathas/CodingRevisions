def string_permutation(s1: str, s2: str):
    hmap_s1 = {}
    hmap_s2 = {}
    for i in range(len(s1)):
        if s1[i] in hmap_s1:
            hmap_s1[s1[i]] += 1
        else:
            hmap_s1[s1[i]] = 1

    for i in range(len(s1)):
        if s2[i] in hmap_s2:
            hmap_s2[s2[i]] += 1
        else:
            hmap_s2[s2[i]] = 1
    k = len(s1)
    print(hmap_s1, hmap_s2)
    if hmap_s2 == hmap_s1:
        return True

    for i in range(k, len(s2)):
        print(s2[i - k])
        if s2[i - k] in hmap_s2:
            hmap_s2[s2[i - k]] -= 1
            if hmap_s2[s2[i - k]] == 0:
                hmap_s2.pop(s2[i - k])
        print(hmap_s2)
        if s2[i] in hmap_s2:
            hmap_s2[s2[i]] += 1
        else:
            hmap_s2[s2[i]] = 1
        # print(hmap_s1, hmap_s2)
        if hmap_s2 == hmap_s1:
            return True

    return False

if __name__ == '__main__':
    print(string_permutation("adc", "dcda"))
