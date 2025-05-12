def merge_intervals(intervals: list):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
    :param intervals:
    :return:
    """
    if not intervals:
        return []

        # Sort intervals by their start times
    intervals.sort(key=lambda x: x[0])  # Sorting ensures we process intervals in order

    result = [intervals[0]]  # Initialize the output list with the first interval

    for i in range(1, len(intervals)):  # Start iterating from the second interval
        current = intervals[i]  # Current interval
        previous = result[-1]  # Last interval in the result list

        # Check if the current interval overlaps with the previous one
        if current[0] <= previous[1]:  # Overlap condition
            # Merge the intervals by updating the end time of the previous interval
            previous[1] = max(previous[1], current[1])
        else:
            # No overlap, add the current interval to the result list
            result.append(current)
    return result

if __name__ == '__main__':
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
    print(merge_intervals([[1,4],[4,5]]))
    print(merge_intervals([[1,4],[0,1]]))
    print(merge_intervals([[2,3],[4,5],[6,7],[8,9],[1,10]]))

