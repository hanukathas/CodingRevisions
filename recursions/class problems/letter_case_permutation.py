def letter_case_permutation(S: str):
    result = set()

    def helper(ip: str, i: int, slate: str):
        if i == len(ip):
            result.add(slate)
            return
        if ip[i] == int:
            helper(ip, i + 1, slate + ip[i])
        helper(ip, i + 1, slate + str(ip[i]).lower())
        helper(ip, i + 1, slate + str(ip[i]).upper())

    helper(S, 0, "")
    return list(result)


def letter_case_permutation_efficient_revision(S: str):
    result = []

    def helper(ip, i: int):
        if i == len(ip):
            result.append("".join(ip[:]))
            return
        if str(ip[i]).isdigit():
            helper(ip, i + 1)
        else:
            ip[i] = str(ip[i]).lower()
            helper(ip, i + 1)
            ip[i] = str(ip[i]).upper()
            helper(ip, i + 1)

    helper(list(S), 0)
    return result


def letter_case_permutation_efficient_revision2(s: str):
    result = []

    def helper(slist: list, i: int):
        if i == len(slist):
            result.append("".join(slist[:]))
            return
        if str(slist[i]).isdigit():
            helper(slist, i + 1)
        else:
            slist[i] = str(slist[i]).lower()
            helper(slist, i + 1)
            slist[i] = str(slist[i]).upper()
            helper(slist, i + 1)

    helper(list(s), 0)
    return result


def letter_case_permutation_efficient_revision3(s: str):
    result = []

    def helper(i, slate):
        if i == len(slate):
            result.append("".join(slate[:]))
            return
        elif str(slate[i]).isdigit():
            helper(i + 1, slate)
        else:
            slate[i] = str(slate[i]).lower()
            helper(i + 1, slate)
            slate[i] = str(slate[i]).upper()
            helper(i + 1, slate)

    helper(0, list(s))
    return result


if __name__ == '__main__':
    print(letter_case_permutation("a1B2"))
    print(letter_case_permutation_efficient_revision3("a1B2"))
