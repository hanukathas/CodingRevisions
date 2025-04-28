def longestPalindrome(s: str):
    if not s:
        return ""

    def helper(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    end = 0
    for i in range(len(s)):
        odd = helper(i, i)
        even = helper(i, i + 1)

        max_len = max(odd, even)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]


def longestPalindrome_leetcode_soln(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    end = 0

    for i in range(len(s)):
        # Check for odd length palindromes
        len1 = expand_around_center(i, i)
        # Check for even length palindromes
        len2 = expand_around_center(i, i + 1)

        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]
if __name__ == '__main__':
    print(longestPalindrome_leetcode_soln("babad"))
    print(longestPalindrome("babad"))