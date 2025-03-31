from collections import deque


def moving_average_window(arr: list, size: int):
    a = deque()
    running_sum = 0
    max_avg = 0
    for i in range(len(arr)):
        a.append(arr[i])
        running_sum += arr[i]
        if len(a) > size:
            running_sum -= a.popleft()
            max_avg = max(max_avg, running_sum / len(a))
            print(a, running_sum / len(a), max_avg)
    return running_sum / len(a)


def moving_average_window_revision(arr: list, size: int):
    queue = deque()
    running_sum = 0
    max_avg = 0
    for i in range(len(arr)):
        queue.append(arr[i])
        running_sum += arr[i]
        if len(queue) == size:
            running_sum -= queue.popleft()
            max_avg = max(max_avg, running_sum / len(queue))

    return max_avg


def max_avg_subarray(arr: list, k: int) -> int:
    running_sum = sum(arr[:k])
    max_avg = running_sum / k

    for i in range(k, len(arr)):
        running_sum = running_sum - arr[i - k] + arr[i]
        max_avg = max(max_avg, running_sum / k)

    return max_avg


if __name__ == '__main__':
    print(f"final ave:{moving_average_window([5, 4, 6, 6, 3, 2], 3)}")
    print(f"final ave:{max_avg_subarray([1, 12, -5, -6, 50, 3], 4)}")
    print(f"final ave:{moving_average_window_revision([5, 4, 6, 6, 3, 2], 3)}")
