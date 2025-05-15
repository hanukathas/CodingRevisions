from trees.path_sum import result


def insert_interval(intervals: list, newInterval: list):
    break_index = -1
    result = []
    for i in range(len(intervals)):
        if intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
        else:
            break_index = i
            break
    if break_index == -1:
        result.append(newInterval)
        return result
    result.append(newInterval)
    for i in range(break_index, len(intervals)):
        if result[-1][1] >= intervals[i][0]:
            result[-1][0] = min(result[-1][0], intervals[i][0])
            result[-1][1] = max(result[-1][1], intervals[i][1])
        else:
            result.append(intervals[i])

    return result

if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(insert_interval(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(insert_interval(intervals, newInterval))

    intervals = [[1,5]]
    newInterval = [6,8]
    print(insert_interval(intervals, newInterval))


