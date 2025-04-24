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

        if len(a) == size:
            if running_sum > upper:
                points += 1
            if running_sum < lower:
                points -= 1


    return points

def diet_plan_revision(arr:list, size: int, upper: int, lower: int):
    running_sum = sum(arr[:size])

    performance = 0
    if running_sum < lower:
        performance -= 1
    elif running_sum > upper:
        performance += 1


    for i in range(size, len(arr)):
        running_sum = running_sum - arr[i - size] + arr[i]

        if running_sum < lower:
            performance -= 1
        elif running_sum > upper:
            performance += 1

    return performance

if __name__ == '__main__':
    # print(diet_plan([1,2,3,4,5], 1, 3, 3))
    print(diet_plan_revision([6,5,0,0], 2, 4, 4))


