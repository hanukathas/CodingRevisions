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
    print(f"final queue: {a}")
    return running_sum / len(a)

if __name__ == '__main__':
    print(f"final ave:{moving_average_window([5,4,6,6,3,2], 3)}")
