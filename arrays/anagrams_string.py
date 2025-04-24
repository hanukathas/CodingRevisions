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
    count = 0
    if hmap_str2 == hmap_str1:
        locations.append(0)
        count += 1

    for i in range(k, len(str2)):
        if str2[i - k] in hmap_str2:
            hmap_str2[str2[i - k]] -= 1
            if hmap_str2[str2[i - k]] == 0:
                hmap_str2.pop(str2[i - k])

        if str2[i] in hmap_str2:
            hmap_str2[str2[i]] += 1
        else:
            hmap_str2[str2[i]] = 1
        # print(hmap_str1, hmap_str2)
        if hmap_str2 == hmap_str1:
            locations.append(i-k)
            count += 1
    return locations, count

def find_anagrams_pos(s1:str, s2:str) -> list:
    output = []
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
    print(hmap_s2, hmap_s1)
    if hmap_s1 == hmap_s2:
        output.append(0)

    print(output)
    k = len(s1)
    for i in range(k, len(s2)):
        if s2[i-k] in hmap_s2:
            hmap_s2[s2[i-k]] -= 1
            if hmap_s2[s2[i-k]] == 0:
                hmap_s2.pop(s2[i-k])
        if s2[i] in hmap_s2:
            hmap_s2[s2[i]] += 1
        else:
            hmap_s2[s2[i]] = 1

        if hmap_s2 == hmap_s1:
            output.append(i - k + 1)
    return output

if __name__ == '__main__':
    # print(anagrams_string("el", "hellelo"))
    print(anagrams_string("ll", "hellelo"))
    # print(find_anagrams_pos("ll", "hellelo"))