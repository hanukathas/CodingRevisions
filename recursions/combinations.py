test1 = [4, 2]


def combination_simple(n, k):
    result = []

    def helper(number, i, slate):
        if len(slate) == k:
            result.append(slate[:])
            return
        for pick in range(i, n + 1):
            slate.append(pick)
            helper(number, i + 1, slate)
            slate.pop()

    helper(n, 1, [])
    return result


def generate_combinations(arr, k):
    # Base cases
    if k == 0:
        return [[]]
    if len(arr) < k:
        return []

    # Recursive cases
    # Take first element
    first = arr[0]
    # Get combinations including first element
    include_first = [[first] + comb for comb in generate_combinations(arr[1:], k - 1)]
    # Get combinations excluding first element
    exclude_first = generate_combinations(arr[1:], k)

    return include_first + exclude_first


# Example usage



if __name__ == '__main__':
    print(combination_simple(test1[0], test1[1]))
    arr = [i + 1 for i in range(test1[0])]
    print(arr)
    print(generate_combinations(arr, test1[1]))
