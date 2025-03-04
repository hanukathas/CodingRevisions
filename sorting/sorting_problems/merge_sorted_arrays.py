test_first = [1, 3, 5]
test_second = [2, 4, 6, 0, 0, 0]
test3 = [1]
test4 = [1,0]


def merge_sorted_arrays(first:[], second:[]) -> []:
    final_array = []
    i = j = 0
    while i < len(first) and j < len(second):
        if first[i] == 0:
            i += 1
        elif second[j] == 0:
            j += 1
        elif second[j] > first[i]:
            final_array.append(first[i])
            i += 1
        else:
            final_array.append(second[j])
            j += 1
    while i < len(first):
        if first[i] != 0:
            final_array.append(first[i])
        i += 1
    while j < len(second):
        if second[j] != 0:
            final_array.append(second[j])
        j += 1
    return final_array

if __name__ == '__main__':
    print(merge_sorted_arrays(test3, test4))