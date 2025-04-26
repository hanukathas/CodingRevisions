def maximal_score_good_subarray(nums: list, k: int):
    """
    step 1: calculate left span: elements lesser than left of i
    step 2: calculate right span: element lesser than right of i
    step 3: calculate area that goes through k: (i - left_span + 1, k, i + right_span - 1)
    :param nums:
    :param k:
    :return:
    """
    n = len(nums)
    left_span = right_span = [0] * n
    left_stack = right_stack = []

    for i in range(n):
        if left_stack and left_stack[-1][0] >= nums[i]:
            left_stack.pop()

        if left_stack:
            left_span = left_stack[-1][1] - i
        else:
            left_span = i + 1
        left_stack.append((nums[i], i))

    for i in range(n):
        if right_stack and right_stack[-1][0] >= nums[i]:
            right_stack.pop()

        if right_stack:
            right_span = i - right_stack[-1][1]
        else:
            right_span = n - i
        right_stack.append((nums[i], i))
    max_score_good = 0
    for i in range(len(nums)):
        area = nums[i] * (left_span[i] + right_span[i] - 1)
        if i - left_span + 1 < k < i + right_span - 1:
            max_score_good = max(max_score_good, area)
    return max_score_good





