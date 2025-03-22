def permutations_immutable(arr: list):
    """
        immutable is when the array elements cannot have their locations changed
    :param arr:
    :return:
    """
    result = []
    def helper(ip, slate):
        if len(ip) == 0:
            result.append(slate)
            return
        for i in range(len(ip)):
            helper(ip[:i]+ip[i+1:], slate + [ip[i]])
    helper(arr, [])
    return result
def permutations_immutable_revision(arr: list):
    result = []
    def helper(ip, slate):
        if len(ip) == 0:
            result.append(slate)
            return
        else:
            for i in range(len(ip)):
                helper(ip[:i]+ip[i+1:], slate+[ip[i]])

    helper(arr, [])
    return result

def permutations_mutable(arr: list):
    """
        the numbers can be picked from the list of remaining elements.
        reduces the complexity to n!*n. this because for the remaining numbers,
        a single unit of complexity is run
    :param arr:
    :return:
    """
    result = []
    def helper(ip: list, i:int):
        if i == len(ip):
            result.append(ip[:])
            return
        for pick in range(i, len(ip)):
            ip[pick], ip[i] = ip[i], ip[pick]
            helper(ip, i+1)
            ip[pick], ip[i] = ip[i], ip[pick]

    helper(arr, 0)
    return result

def permutations_mutable_all_in_revision(arr: list):
    result = []
    def helper(ip, i):
        if i == len(ip):
            result.append(ip[:])
            return
        else:
            hmap = {}
            for pick in range(i, len(ip)):
                if ip[pick] not in hmap:
                    hmap[ip[pick]] = 1
                    ip[pick], ip[i] = ip[i], ip[pick]
                    helper(ip, i + 1)
                    ip[pick], ip[i] = ip[i], ip[pick]




    helper(arr, 0)
    return result


def permutations_mutable_non_distinct_numbers(arr: list):
    """
        the numbers can be picked from the list of remaining elements.
        reduces the complexity to n!*n. this because for the remaining numbers,
        a single unit of complexity is run
    :param arr:
    :return:
    """
    result = []
    def helper(ip: list, i:int):
        if i == len(ip):
            result.append(ip[:])
            return
        for pick in range(i, len(ip)):
            hmap = {}
            if ip[pick] not in hmap:
                hmap[ip[pick]] = 1
                ip[pick], ip[i] = ip[i], ip[pick]
                helper(ip, i + 1)
                ip[pick], ip[i] = ip[i], ip[pick]

    helper(arr, 0)
    return  result


if __name__ == '__main__':
    print(permutations_immutable_revision([1,2,3]))
    print(permutations_mutable([1, 2, 3]))
    print(permutations_mutable_all_in_revision([1, 2, 3]))
    print(permutations_mutable_all_in_revision([1, 1, 3]))