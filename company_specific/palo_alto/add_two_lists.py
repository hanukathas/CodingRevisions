def add_two_lists(list1, list2):
    """
    Adds two lists element-wise. If the lists are of different lengths,
    the shorter one is padded with zeros.

    Args:
        list1 (list): The first list of numbers.
        list2 (list): The second list of numbers.

    Returns:
        list: A new list containing the element-wise sums.
    """
    len1 = len(list1) - 1
    len2 = len(list2) - 1

    carry_on = 0

    result = []

    while len1 >= 0 or len2 >= 0 or carry_on:
        # print(list2[len2], list1[len1])
        l1 = 0
        l2 = 0
        if len2 < 0:
            l2 = 0
        else:
            l2 = list2[len2]

        if len1 < 0:
            l1 = 0
        else:
            l1 = list1[len1]

        print(l1, l2)
        s = l1 + l2 + carry_on
        carry_on = s // 10
        r = s % 10

        result.append(r)
        len2 -= 1
        len1 -= 1
    result.reverse()
    return result

if __name__ == '__main__':
    list1 = [1, 9, 9, 9]
    list2 = [9, 0, 9]
    print(add_two_lists(list1, list2))
