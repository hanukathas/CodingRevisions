def anagrams_string(str1, str2):
    hmap_str1 = {}
    hmap_str2 = {}
    locations = []
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
        locations.append(0)

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
            locations.append(i-k)
    return locations

if __name__ == '__main__':
    print(anagrams_string("el", "hellelo"))