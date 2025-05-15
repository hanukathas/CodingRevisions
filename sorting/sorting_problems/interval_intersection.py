def interval_intersection(first: list, second: list):
    i , j = 0, 0
    result = []
    while i < len(first) and j < len(second):
        if first[i][1] < second[j][0]:
            i += 1
        elif second[j][1] < first[i][0]:
            j += 1
        else:
            record = (max(first[i][0], second[j][0]), min(first[i][1], second[j][1]))
            result.append(record)

            if first[i][1] <= second[j][1]:
                # second interval of first is less than second interval of first then there are no overlaps
                i += 1
            else:
                j += 1
    return result

if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15,24],[25,26]]

    print(interval_intersection(firstList, secondList))
