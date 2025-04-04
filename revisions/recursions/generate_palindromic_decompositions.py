
def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    result = []
    def is_palindrome(start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    def helper(start, slate):
        if start == len(s):
            result.append(slate[:])
            return
        for end in range(start, len(s)):
            if is_palindrome(start, end):
                slate.append(s[start:end+1])
                helper(end+1, slate)
                slate.pop()
    helper(0, [])
    return result

if __name__ == '__main__':
    s = "abracadabra"
    result = generate_palindromic_decompositions(s)
    print("All palindromic decompositions:", result)