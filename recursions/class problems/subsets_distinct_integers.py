def subsets_distinct_integers_immutable(S: list):
    result = list()

    def helper(ip: list, i: int, slate):
        if i == len(ip):
            result.append(slate)
            return
        helper(ip, i+1, slate)

        helper(ip, i+1, slate  + [ip[i]]) # remember the list part
    helper(S, 0, [])
    return result

def subsets_distinct_integers_mutable(S: list):
    result = list()

    def helper(ip: list, i: int, slate):
        if i == len(ip):
            result.append(slate[:])
            return
        helper(ip, i + 1, slate)
        slate.append(ip[i])
        helper(ip, i + 1, slate)
        slate.pop()
    helper(S, 0, [])
    return result

def subsets_distinct_integers_mutable_revision(S: list):
    result = []
    def helper(i, slate):
        if i == len(S):
            result.append(slate[:])
            return

        helper(i+1, slate)
        slate.append(S[i])
        helper(i + 1, slate)
        slate.pop()
    helper(0, [])
    return result


if __name__ == '__main__':
    print(subsets_distinct_integers_immutable([1,2,3]))
    print(subsets_distinct_integers_mutable([1, 2, 3]))
    print(subsets_distinct_integers_mutable_revision([1, 2, 3]))