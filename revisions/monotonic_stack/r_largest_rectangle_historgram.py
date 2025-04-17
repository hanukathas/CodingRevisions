def r_largest_rectangle_historgram(historgram: list):
    n = len(historgram)
    left_span = [0] * n
    historgram_stack = []
    for i in range(n):
        while historgram_stack and historgram_stack[-1][0] >= historgram[i]:
            historgram_stack.pop()

        if historgram_stack:
            left_span[i] = i - historgram_stack[-1][1]
        else:
            left_span[i] = i + 1

        historgram_stack.append(( historgram[i], i))

    right_span = [0] * n
    histogram_stack_right = []
    for i in range(n-1, -1, -1):
        while histogram_stack_right and histogram_stack_right[-1][0] >= historgram[i]:
            histogram_stack_right.pop()
        if histogram_stack_right:
            right_span[i] = histogram_stack_right[-1][1] - i
        else:
            right_span[i] = n - i
        histogram_stack_right.append((historgram[i], i))

    max_area = 0
    for i in range(n):
        area = historgram[i] * (left_span[i] + right_span[i] - 1)
        max_area = max(max_area, area)

    return max_area

if __name__ == '__main__':
    print(r_largest_rectangle_historgram([2,1,5,6,2,3]))




