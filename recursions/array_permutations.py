def get_permutations(arr):
    if len(arr) <= 1:
        return [arr]

    result = []

    for i in range(len(arr)):
        slate = arr[i]
        remaining = arr[:i]+arr[i+1:]
        for p in get_permutations(remaining):
            result.append([slate]+p)
    return result

def get_permutations_revision(arr: []):
    if len(arr) <= 1:
        return [arr]
    result = []
    for i in range(len(arr)):
        slate = arr[i]
        remaining = arr[:i]+arr[i+1:]
        for p in get_permutations_revision(remaining):
            result.append([slate]+p)
    return result

def get_permutations_revision2(arr: []):
    if len(arr) <= 1:
        return [arr]
    result = list()
    hmap = {}
    for i in range(len(arr)):
        if arr[i] not in hmap:
            hmap[arr[i]] = 1
            slate = arr[i]
            remaining = arr[:i]+arr[i+1:]
            for p in get_permutations_revision2(remaining):
                result.append([slate] + p)
    return result


if __name__ == '__main__':
    print(get_permutations([1,2,2]))
    print(get_permutations_revision2([1, 2, 2]))