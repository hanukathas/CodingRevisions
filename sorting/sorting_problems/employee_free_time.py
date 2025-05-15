from typing import List


def employeeFreeTime(schedule: List[List[List[int]]]) -> List[List[int]]:
    # Flatten and sort all intervals
    events = []
    for employee in schedule:
        for interval in employee:
            events.append((interval[0], 1))  # 1 for start
            events.append((interval[1], -1))  # -1 for end

    events.sort()  # Sort by time
    print(events)
    result = []
    ongoing = 0  # Count of ongoing meetings
    prev_time = None

    for time, delta in events:
        # Found a gap between meetings
        print(ongoing, prev_time, result)
        if ongoing == 0 and prev_time is not None and prev_time < time:
            result.append([prev_time, time])

        ongoing += delta
        prev_time = time

    return result

if __name__ == '__main__':
    schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
    print(employeeFreeTime(schedule))  # Output: [[3,4]]

    # schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2,5],[9,12]]]
    # print(employeeFreeTime(schedule))
