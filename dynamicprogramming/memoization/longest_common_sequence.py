def longest_common_sequence(first: str, second: str, i: int, j: int, mem:{}) -> int:
    if i >= len(first) or j >= len(second):
        return 0
    key = f"{i},{j}"
    if key in mem:
        return mem[key]
    else:
        if first[i] == first[j]:
            mem[key] = 1 + longest_common_sequence(first, second, i+1, j+1, mem)
        else:
            max(
                longest_common_sequence(first, second, i+1, j, mem),
                longest_common_sequence(first, second, i, j+1, mem)
            )
        return mem[key]

def lcs_memo(str1, str2, i=0, j=0, memo={}):
    key = f"{i},{j}"
    if key in memo:
        return memo[key]
    if i == len(str1) or j == len(str2):
        return 0
    if str1[i] == str2[j]:
        memo[key] = 1 + lcs_memo(str1, str2, i+1, j+1, memo)
    else:
        memo[key] = max(
            lcs_memo(str1, str2, i+1, j, memo),
            lcs_memo(str1, str2, i, j+1, memo)
        )
    return memo[key]

if __name__ == '__main__':
    print(longest_common_sequence("hello", "llo", 0, 0, {}))
    print(lcs_memo("hello", "llo", 0,0, {}))
