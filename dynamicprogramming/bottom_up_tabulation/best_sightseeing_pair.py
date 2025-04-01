def best_sightseeing_pair(values: list):
    max_so_far = values[0] + 0
    result = float('-inf')

    for j in range(1, len(values)):
        result = max(result, max_so_far + values[j] -j)
        max_so_far = max(max_so_far, values[j] + j)

    return result

def best_sightseeing_pair_revision(values: list):
    max_so_far = values[0] + 0
    result = max_so_far
    for j in range(1, len(values)):
        result = max(result, max_so_far + values[j] - j)
        max_so_far = max(max_so_far, values[j] + j)
    return result



if __name__ == '__main__':
    print(best_sightseeing_pair([8,1,5,2,6]))
    print(best_sightseeing_pair_revision([8, 1, 5, 2, 6]))