test1 = [4, 2]

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
def combine_simple_revision(n,k):
    result = []
    def helper(i, slate):
        if len(slate) == k:
            result.append(slate[:])
            return
        for pick in range(i, n+1):
            slate.append(pick)
            helper(i+1, slate)
            slate.pop()
    helper(1, [])
    return result

if __name__ == '__main__':
    print(combine_simple(test1[0], test1[1]))
    print(combine_simple_revision(test1[0], test1[1]))
