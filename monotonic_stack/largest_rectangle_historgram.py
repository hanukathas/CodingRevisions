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
    for i in range(n):
        while histogram_stack_right and histogram_stack_right[-1][0] >= histogram[i]:
            histogram_stack_right.pop()
        if histogram_stack_right:
            right_span[i] = histogram_stack_left[-1][1] - i   # distance from current pointer to position where the value is lesser
        else:
            right_span[i] = n - i
        histogram_stack_left.append((histogram[i], i))
    largest_rectangle = 0
    for i in range(n):
        area = histogram[i] * (left_span[i] + right_span[i] - 1)
        largest_rectangle = max(largest_rectangle, area)
    return largest_rectangle

if __name__ == '__main__':
    print(largest_rectangle_historgram([4,4]))









