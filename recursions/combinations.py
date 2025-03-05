test1 = [5,3]

def combine(n, k):
    result = []
    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in (start, n+1):
            path.append(i)
            backtrack(i+1, path)
            path.pop()
    backtrack(1, [])
    return result


if __name__ == '__main__':
    print(combine(test1[0], test1[1]))