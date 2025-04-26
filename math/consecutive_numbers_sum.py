def consecutive_numbers_sum(N: int):
    """
    N = a + a + 1 + a + 2 ...+ a + k - 1
    N = ka + k(k-1)/2
    N - k(k-1)/2 = ka
    (N - k(k-1)/2) / k = a
    we need to find all a's such that (N - k(k-1)/2) % k = 0 because if we find an a,
    the sum equals N and the difference will be 0
    :param N:
    :return:
    """
    k = 1  # base case
    total = 0  # number of a's initially

    while (N - k * (k - 1) // 2) > 0:  # sum of consecutive numbers can't be greater than k
        if (N - k * (k - 1) // 2) % k == 0:
            total += 1
        k += 1

    return total


def consecutive_numbers_sum_r(N: int):
    """
    https://leetcode.com/problems/consecutive-numbers-sum/description/
    :param N:
    :return:
    """
    k = 1
    a = 0


    while (N - k * (k - 1) // 2) > 0:

        if (N - k * (k - 1) // 2) % k == 0:
            a += 1
        k += 1
    return a

if __name__ == '__main__':
    print(consecutive_numbers_sum(5))
    print(consecutive_numbers_sum_r(5))