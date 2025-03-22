# this can be solved as an immutable set since we can pick choose elements
def subset_sum_equals_k(arr: list, k: int):
    result = []
    def helper(ip, i, slate, slatesum):
        if slatesum == k:
            result.append(slate[:])
            return 1
        if slatesum > k:

            return 0
        if len(slate) == len(ip):
            return 0
        if i == len(arr):
            return 0

        return helper(ip, i+1, slate, slatesum) + helper(ip, i+1, slate + [ip[i]], slatesum+ip[i])
    helper(arr, 0, [], 0)
    return result

def subset_sum_equals_k_revision(arr: list, k: int):
    result = []
    def helper(ip, i, slate, slatesum):
        if slatesum == k:
            result.append(slate[:])
            return 1
        if slatesum > k:
            return 0
        if i == len(ip):
            return 0
        else:
            return helper(ip, i+1, slate, slatesum) + helper(ip, i+1, slate+[ip[i]], slatesum+ip[i])
    helper(arr, 0, [], 0)
    return result




if __name__ == '__main__':
    print(subset_sum_equals_k([10,1,2,7,6,1,5], 8))
    print(subset_sum_equals_k_revision([10, 1, 2, 7, 6, 1, 5], 8))