def longest_substring_without_repeating(s: str):
    hmap = {}
    left = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] in hmap:
            hmap[s[i]] += 1
        else:
            hmap[s[i]] = 1

        while left <= i and hmap[s[i]] > 1:
            if s[left] in hmap:
                hmap[s[left]] -= 1
                if hmap[s[left]] == 0:
                    hmap.pop(s[left])
            left += 1


        max_length = max(max_length, i - left + 1)

    return max_length

if __name__ == '__main__':
    print(longest_substring_without_repeating("abcabcbb"))
    print(longest_substring_without_repeating("bbbbb"))
    print(longest_substring_without_repeating("bbbbb"))