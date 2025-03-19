test1 = [4, 2]


def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in (start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result

def combine_simple(n,k):
    result = []
    def helper(number, i, slate):
        if len(slate) == k:
            result.append(slate[:])
            return
        for pick in range(i, n+1):
            slate.append(pick)
            helper(number, i+1, slate)
            slate.pop()
    helper(n, 1, [])
    return result


if __name__ == '__main__':
    print(combine(test1[0], test1[1]))
    print(combine_simple(test1[0], test1[1]))
