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
def subset_sum_equals_k_revision(arr, k):
    result = []
    def helper(ip, i, slate, slatesum):
        if slatesum == k:
            result.append(slate[:])
            return 1
        if slatesum > k:
            return 0
        if len(slate) == len(ip):
            return 0
        if i == len(ip):
            return 0
        return helper(ip, i+1, slate, slatesum) + helper(ip, i+1, slate+[arr[i]], slatesum+arr[i])
    helper(arr, 0,[],0)
    return result

def subset_sum_equals_k_revision2(arr, k):
    result = []
    def helper(i, slate, slate_sum):
        if k == slate_sum:
            if slate[:] not in result:
                result.append(sorted(slate[:]))
            return 1
        if slate_sum > k:
            return 0
        if i == len(arr):
            return 0
        if len(slate) == len(arr):
            return 0

        return helper(i+1, slate, slate_sum) + helper(i+1, slate+[arr[i]], slate_sum+arr[i])

    helper(0, [], 0)
    return list(result)

def subset_sum_equals_k_r(arr, k):
    result = []
    def helper(i, slate, slatesum):
        if slatesum == k:
            if slate[:] not in result:
                result.append(sorted(slate[:]))
            return 1
        if slatesum > k:
            return 0
        if i == len(arr):
            return 0
        if len(arr) == len(slate):
            return 0
        return helper(i + 1, slate, slatesum) + helper(i + 1, slate + [arr[i]], slatesum + arr[i])
    helper(0, [], 0)
    return result


if __name__ == '__main__':
    print(subset_sum_equals_k([10,1,2,7,6,1,5], 8))
    print(subset_sum_equals_k_revision2([10,1,2,7,6,1,5], 8))

    print(subset_sum_equals_k_r([10, 1, 2, 7, 6, 1, 5], 8))