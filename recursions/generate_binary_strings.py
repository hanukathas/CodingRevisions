test1 = 3


def bs_helper(n: int, result: list, slate: str):
    if n == 1:
        result.append(slate + "0")
        result.append(slate + "1")
        print(f"{result} for n = 1")
    else:
        bs_helper(n - 1, result, slate + "0")
        print(f"{result} for slate = 0")
        bs_helper(n - 1, result, slate + "1")
        print(f"{result} for slate = 1")
    return result


def bs_helper_revision(n: int, result: list, slate: str):
    if n == 1:
        result.append(slate + "0")
        result.append(slate + "1")

    else:
        bs_helper_revision(n - 1, result, slate + "0")
        bs_helper_revision(n - 1, result, slate + "1")
    return result


def bs_helper_r(n: int, result: list, slate: str):
    if n == 1:
        result.append(slate + "0")
        result.append(slate + "1")
    else:
        bs_helper_r(n - 1, result, slate + "0")
        bs_helper_r(n - 1, result, slate + "1")
    return result


def get_binary_strings(n):
    # return bs_helper_revision(n, [], "")
    return bs_helper_r(n, [], "")


if __name__ == '__main__':
    print(get_binary_strings(4))
    print(get_binary_strings(2))
