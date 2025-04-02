def generate_parenthesis(n):
    result = []

    def helper(nleft, nright, slate):
        if nleft == 0 and nright == 0:
            result.append("".join(slate[:]))
            return
        if nleft > nright or nright < nleft or nleft < 0 or nright < 0:
            return
        slate.append('{')
        helper(nleft-1, nright, slate)
        slate.pop()

        slate.append('}')
        helper(nleft, nright - 1, slate)
        slate.pop()

    helper(n, n, [])
    return result

def generate_parenthesis_revision(n):
    result = []
    def helper(nleft, nright, slate):
        if nleft == nright == 0:
            result.append(slate[:])
            return
        if nleft < nright or nright < nleft or nleft < 0 or nright < 0:
            return
        slate.append('{')
        helper(nleft+1, nright, slate)
        slate.pop()

        slate.append('{')
        helper(nleft+1, nright, slate)
        slate.pop()

    helper(n, n, [])
    return result



if __name__ == '__main__':
    print(generate_parenthesis(3))