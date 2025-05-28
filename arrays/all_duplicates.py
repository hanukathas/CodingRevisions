


def all_duplicates(arr: list):
    for i in range(len(arr)):
        while arr[i] != i+1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break
    result = []
    for i in range(len(arr)):
        if arr[i] != i+1:
            result.append(arr[i])
    return result

def all_duplicates_revision(arr: list):
    result = []
    for i in range(len(arr)):
        while arr[i] != i+1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[i], arr[d] = arr[d], arr[i]
            else:
                break
    for i in range(len(arr)):
        if arr[i] != i + 1:
            result.append(arr[i])
    return result

def all_duplicates_revision_2(arr: list):
    result = []
    for i in range(len(arr)):
        while arr[i] != i + 1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[d], arr[i] = arr[i], arr[d]
            else:
                break
    for i in range(len(arr)):
        if arr[i] != i+1:
            result.append(arr[i])
    return result

def duplicates(arr: list):
    if len(arr) <= 1:
        return arr
    dup_result = []
    for i in range(len(arr)):
        while arr[i] != i + 1:
            d = arr[i] - 1
            if arr[d] != arr[i]:
                arr[d], arr[i] = arr[i], arr[d]
            else:
                break
    for i in range(len(arr)):
        if arr[i] != i+1:
            dup_result.append(arr[i])
    return dup_result



if __name__ == '__main__':
    print(all_duplicates([1,2,4,3,4]))
    print(all_duplicates_revision([1, 2, 4, 3, 4]))
    print(all_duplicates_revision_2([1, 2, 4, 3, 4]))