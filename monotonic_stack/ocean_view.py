from collections import deque

def ocean_view(arr: list):
    max_height = arr[-1]
    stack = deque()
    stack.appendleft(len(arr) - 1)
    for i in range(arr[-2],-1, -1):
        if arr[i] > max_height:
            max_height = arr[i]
            stack.appendleft(i)

    return list(stack)

# monotonic stack method
def ocean_view_ms(heights: list):
    view_stack = []

    for i in range(len(heights)):
        while view_stack and view_stack[-1][0] < heights[i]:
            view_stack.pop()
        view_stack.append((heights[i], i))
    result = []
    for i in range(len(view_stack)):
        result.append(view_stack[i][1])

    return result

if __name__ == '__main__':
    # print(ocean_view([10,9,1,3]))
    print(ocean_view_ms([10, 9, 1, 3]))
