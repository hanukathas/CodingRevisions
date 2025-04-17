def r_ocean_view(heights: list):
    ocean_view_stack = []
    views = []

    for i in range(len(heights)):
        while ocean_view_stack and ocean_view_stack[-1][0] <= heights[i]:
            ocean_view_stack.pop()

        ocean_view_stack.append((heights[i], i))
    print(ocean_view_stack)
    for i in range(len(ocean_view_stack)):
        views.append(ocean_view_stack[i][1])

    return views

if __name__ == '__main__':
    # print(ocean_view([10,9,1,3]))
    print(r_ocean_view([10, 9, 1, 3]))



