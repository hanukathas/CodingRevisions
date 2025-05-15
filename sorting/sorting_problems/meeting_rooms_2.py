import heapq
from collections import deque
from itertools import count


def meeting_rooms_2(intervals: list):
    """
    https://leetcode.com/problems/meeting-rooms-ii/description/
    :param intervals:
    :return:
    """
    # Edge case: if no intervals, return 0
    start_timings = sorted(intervals[i][0] for i in range(len(intervals)))
    end_timings = sorted(intervals[i][1] for i in range(len(intervals)))

    rooms_needed = 0
    max_rooms_needed = 0

    start_ptr, end_ptr = 0, 0

    while start_ptr < len(intervals):
        # do I need a new room
        if start_timings[start_ptr] <= end_timings[end_ptr]:
            rooms_needed += 1
            start_ptr += 1
        else: # can I reuse a room
            rooms_needed -= 1
            end_ptr += 1
        max_rooms_needed = max(max_rooms_needed, rooms_needed)
    return max_rooms_needed






if __name__ == '__main__':
    print(meeting_rooms_2([[0,30],[5,10],[15,20]]))
    print(meeting_rooms_2([[5,8],[6,8]]))
