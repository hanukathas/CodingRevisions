def find_missing_number(n:int, s: str):
    found = set()
    i = 0

    while i < len(s):
        # Try maximum possible digits that could form a valid number
        for j in range(min(len(str(n)), len(s) - i), 0, -1):
            num = int(s[i:i + j])
            if 1 <= num <= n:
                found.add(num)
                i += j
                break
        else:
            i += 1

    # Find the missing number
    for num in range(1, n + 1):
        if num not in found:
            return num

    return -1

def find_number(n: int, s: str):
    if not n or not s:
        return -1
    i = 0
    numbers = set()
    while i < len(s):
        for j in range(min(len(str(n)), len(s) - i), 0, -1):
            number = int(s[i:i+j])
            if 1 <= number <= n:
                numbers.add(number)
                i += j
                break
        else:
             i += 1
    print(numbers)
    for i in range(1, n + 1):
        if i not in numbers:
            return i



if __name__ == '__main__':
    n1 = 5
    s1 = "1234"
    print(find_number(n1, s1))  # Output: 5

    # Example 2
    n2 = 13
    s2 = "131092345611781"
    print(find_number(n2, s2))  # Output: 12