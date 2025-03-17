from collections import deque


def diet_plan(arr:list, size: int, upper: int, lower: int):
    a = deque()
    running_sum = 0
    points = 0
    for i in range(len(arr)):
        if len(a) == size:
            running_sum -= a.popleft()
        running_sum += arr[i]
        a.append(arr[i])
        print(len(a))
        if len(a) == size:
            if running_sum > upper:
                points += 1
            if running_sum < lower:
                points -= 1
            print(f"running_sum:{running_sum} points:{points} running_sum:{running_sum}")


    return points

if __name__ == '__main__':
    print(diet_plan([1,3,5,0,0,6,7], 2, 5, 0))


