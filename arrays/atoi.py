from trees.path_sum import result


def atoi(s: str):
    s = s.strip()
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    sign = 1
    start_index = 0
    if s[0] == '+' or s[0] == '-':
        start_index = 1
        if s[0] == '-':
            sign = -1
    result = 0

    for i in range(start_index, len(s)):
        if s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
        else:
            break
    return result * sign

if __name__ == '__main__':
    # print(atoi("  -d042hello  "))
    # print(atoi("  -ra0420gamm  "))
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    word = "  -01  "
    word = word.strip()
    sign = 1 if word[0] != '-' else -1
    j = 0
    number = ""
    while j < len(word):
        if word[j] == '0' and number == "":
            j += 1
        else:
            number += '0'
        if word[j].isdigit():
            if int(number) * 10 + int(word[j]) >= INT_MAX:
                number = str(INT_MAX)
            elif int(number) * 10 + int(word[j]) <= INT_MIN:
                number = str(INT_MIN)
            else:
                number +=  word[j]
        else:
            print("done")




