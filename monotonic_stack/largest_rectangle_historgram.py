def largest_rectangle_historgram(histogram: list):
    """
    for a given index, I keep looking left for a number that is lesser than me because
    I can keep including myself as long I see something left
    :param histogram:
    :return:
    """
    n = len(histogram)
    histogram_stack_left = []
    left_span = [0] * n
    # step 1: calculate the left span, smaller elements lefter than ith element
    for i in range(n):
        while histogram_stack_left and histogram_stack_left[-1][0] >= histogram[i]:
            histogram_stack_left.pop()
        if histogram_stack_left:
            left_span[i] = i - histogram_stack_left[-1][1] # distance from current pointer to position where the value is lesser
        else:
            left_span[i] = i + 1
        histogram_stack_left.append((histogram[i], i))

    # step 2: find the right span, smaller than the right ith element
    right_span = [0] * n
    histogram_stack_right = []
    for i in range(n-1, -1, -1):
        while histogram_stack_right and histogram_stack_right[-1][0] >= histogram[i]:
            histogram_stack_right.pop()
        if histogram_stack_right:
            right_span[i] = histogram_stack_right[-1][1] - i   # distance from current pointer to position where the value is lesser
        else:
            right_span[i] = n - i
        histogram_stack_right.append((histogram[i], i))
    largest_rectangle = 0
    for i in range(n):
        area = histogram[i] * (left_span[i] + right_span[i] - 1)
        largest_rectangle = max(largest_rectangle, area)
    return largest_rectangle

def rectangle_histogram(heights: []):
    n = len(heights)
    max_area = 0
    histo_stack = []
    left_span = [0] * n
    right_span = [0] * n

    for i in range(n):
        if histo_stack and histo_stack[-1][0] >= heights[i]:
            histo_stack.pop()
        if histo_stack:
            left_span[i] = i - histo_stack[-1][1]
        else:
            left_span[i] = i + 1
        histo_stack.append([heights[i], i])

    histogram_stack_right = []

    for i in range(n-1, -1, -1):
        if histogram_stack_right and histogram_stack_right[-1][0] >= heights[i]:
            histogram_stack_right.pop()
        if histogram_stack_right:
            right_span[i] = histogram_stack_right[-1][1] - i
        else:
            right_span[i] = n - i
        histogram_stack_right.append([heights[i], i])

    for i in range(n):
        area = (left_span[i] + right_span[i] - 1) * heights[i]
        max_area = max(area, max_area)

    return max_area



if __name__ == '__main__':
    print(largest_rectangle_historgram([2,1,5,6,2,3]))
    print(rectangle_histogram([2, 1, 5, 6, 2, 3]))









