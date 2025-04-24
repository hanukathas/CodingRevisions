def anagrams_string(str1, str2):
    str1_hmap = {}
    str2_hmap = {}

    for i in range(len(str1)):
        if str1[i] not in str1_hmap:
            str1_hmap[str1[i]] = 1
        else:
            str1_hmap[str1[i]] += 1

    for i in range(len(str1)):
        if str2[i] not in str2_hmap:
            str2_hmap[str2[i]] = 1
        else:
            str2_hmap[str2[i]] += 1
    print(str1_hmap)
    print(str2_hmap)
    count = 0
    if str1_hmap == str2_hmap:
        count += 1

    k = len(str1)

    for i in range(k, len(str2)):
        if str2[i - k] in str2_hmap:
            str2_hmap[str2[i - k]] -= 1
            if str2_hmap[str2[i - k]] == 0:
                del str2_hmap[str2[i - k]]
        if str2[i] not in str2_hmap:
            str2_hmap[str2[i]] = 1
        else:
            str2_hmap[str2[i]] = 1

        if str1_hmap == str2_hmap:
            count += 1
    return count

if __name__ == '__main__':
    # print(anagrams_string("el", "hellelo"))
    print(anagrams_string("ll", "llhellelo"))