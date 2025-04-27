def non_overlapping_intervals(intervals: list):
    intervals.sort(key=lambda item: item[1])

    non_overlapping = 1
    interval_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if interval_end <= intervals[i][0]:
            non_overlapping += 1
            interval_end = intervals[i][1]
    return len(intervals) - non_overlapping

def non_overlapping_intervals_r(intervals: list):
    """
    https://leetcode.com/problems/non-overlapping-intervals/description/
    :param intervals:
    :return:
    """
    sorted(intervals, key=lambda items:items[1])

    non_overlaps = 1
    interval_end = intervals[0][1]
    for i in range(1, len(intervals)):
        if interval_end <= intervals[i][0]:
            non_overlaps += 1
            interval_end = intervals[i][1]
    return len(intervals) - non_overlaps


if __name__ == '__main__':
    print(non_overlapping_intervals([[1,2],[2,3],[3,4],[1,3]]))
    print(non_overlapping_intervals([[1,2],[1,2],[1,2]]))

    print(non_overlapping_intervals_r([[1,2],[2,3],[3,4],[1,3]]))
    print(non_overlapping_intervals_r([[1,2],[1,2],[1,2]]))