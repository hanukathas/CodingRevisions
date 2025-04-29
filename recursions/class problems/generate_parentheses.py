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

def generate_parenthesis_r(n):
    result = []
    def helper(n_left, n_right, slate):
        if n_left == 0 and n_right == 0:
            result.append("".join(slate[:]))
            return

        if n_left > n_right or n_right < n_left or n_left < 0 or n_right < 0:
            return

        slate.append('(')
        helper(n_left-1, n_right, slate)
        slate.pop()

        slate.append(')')
        helper(n_left, n_right-1, slate)
        slate.pop()

    helper(n,n, [])
    return result

def generate_parenthesis_revision(n):
    result = []
    def helper(nleft, nright, slate):
        if nleft == nright == 0:
            result.append(slate[:])
            return
        if nleft == 0 or nright == 0 or nright < nleft or nleft < nright:
            return
        slate.append("{")
        helper(nleft-1, nright, slate)
        slate.pop()

        slate.append("}")
        helper(nleft, nright-1, slate)
        slate.pop()

    helper(n,n, [])
    return result



if __name__ == '__main__':
    print(generate_parenthesis_r(3))