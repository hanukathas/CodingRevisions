test1 = 3

def bs_helper(n: int, result: list, slate: str):
    if n == 1:
        result.append(slate+"0")
        result.append(slate+"1")
    else:
        bs_helper(n - 1, result, slate+"0")
        bs_helper(n - 1, result, slate+"1")
    return result

def get_binary_strings(n):
    return bs_helper(n, [], "")

if __name__ == '__main__':
    print(get_binary_strings(3))