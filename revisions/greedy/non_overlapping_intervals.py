def non_overlapping_intervals(intervals: list):
    intervals.sort(key=lambda item: item[1])

    non_overlapping = 1
    interval_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if interval_end <= intervals[i][0]:
            non_overlapping += 1
            interval_end = intervals[i][1]
    return len(intervals) - non_overlapping


