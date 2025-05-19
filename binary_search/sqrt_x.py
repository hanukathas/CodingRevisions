def sqrt_x(x):
    """
    for number k ranging 1 -> x, k has to be a square root if its a perfect square
    :param x:
    :return:
    """
    start = 1
    end = x
    while start <= end:
        mid = start + (end - start) // 2
        sq = mid * mid
        if sq == x:
            return mid
        if sq < x:
            start += 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    print(sqrt_x(18))