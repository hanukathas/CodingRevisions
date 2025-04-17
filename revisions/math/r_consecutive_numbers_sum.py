def r_consecutive_numbers_sum(number: int):
    """
    number = a + a+1 + .... + a + k - 1 = ka + k(k-1)/2; ∴ ka = number - k(k-1)/2 we need to have number - k(k-1)/2 > 0
    also, we can have more than one a
    we need to find a's such that (number - k*(k-1)/2) % k = 0
    :param number:
    :return:
    """
    numbers = 0

    k = 1

    while number - k*(k-1)/2 > 0:
        if (number - k*(k-1)/2) % k == 0:
            numbers += 1
        k += 1

    return numbers

if __name__ == '__main__':
    print(r_consecutive_numbers_sum(3))