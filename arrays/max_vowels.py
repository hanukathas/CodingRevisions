def max_vowels_of_length_k(s: str, k: int):
    vowels = 'aeiou'
    cur_str = s[:k]
    max_vowels = 0
    for i in range(len(cur_str)):

        if cur_str[i] in vowels:
            max_vowels += 1
    for i in range(k, len(s)):
        if s[i] in vowels:
            max_vowels += 1
        if s[i - k] in vowels:
            max_vowels -= 1
    return  max_vowels

def max_vowels_of_length_k_r(s: str, k: int):
    vowels = 'aeiou'
    cur_s = s[:k]
    max_count = 0
    for i in range(len(cur_s)):
        if cur_s[i] in vowels:
            max_count += 1
    print(max_count)
    for  i in range(k, len(cur_s)):
        if s[i] in vowels:
            max_count += 1
        if s[i-k] in vowels:
            max_count -= 1

    return max_count


if __name__ == '__main__':
    print(max_vowels_of_length_k("leetcode", 3))