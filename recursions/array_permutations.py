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



if __name__ == '__main__':
    print(get_permutations([1,2,3]))