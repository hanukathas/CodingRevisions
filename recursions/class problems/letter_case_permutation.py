def letter_case_permutation(S: str):
    result = set()
    def helper(ip: str, i:int , slate: str):
        if i == len(ip):
            result.add(slate)
            return
        if ip[i] == int:
            helper(ip, i+1, slate+ip[i])
        helper(ip, i + 1, slate+str(ip[i]).lower())
        helper(ip, i + 1, slate + str(ip[i]).upper())



    helper(S, 0, "")
    return list(result)

def letter_case_permutation_efficient(S: str):
    result = list()
    def helper(ip, i):
        if i == len(ip):
            result.append("".join(ip))
            return
        if isinstance(ip[i], int):
            helper(ip, i+1)
        else:
            ip[i] = str(ip[i]).lower()
            helper(ip, i+1)
            ip[i] = str(ip[i]).upper()
            helper(ip, i + 1)

    helper(list(S), 0)
    return result

def letter_case_permutation_efficient_revision(S: str):
    result = []
    def helper(ip, i: int):
        if i == len(ip):
            result.append("".join(ip[:]))
            return
        if str(ip[i]).isdigit():
            helper(ip, i+1)
        else:
            ip[i] = str(ip[i]).lower()
            helper(ip, i + 1)
            ip[i] = str(ip[i]).upper()
            helper(ip, i + 1)

    helper(list(S), 0)
    return result


if __name__ == '__main__':
    print(letter_case_permutation("a1B2"))
    print(letter_case_permutation_efficient("a1B2"))
    print(letter_case_permutation_efficient_revision("a1B2"))