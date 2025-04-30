def longestPalindrome(s: str):
    if len(s) <= 1:
        return s
    max_len = 0
    def helper(left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    end = 0

    for i in range(len(s)):
        odd = helper(i, i)
        even = helper(1, i + 1)

        max_len = max(odd, even)
        if max_len > end - start + 1:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2


    return end - start + 1