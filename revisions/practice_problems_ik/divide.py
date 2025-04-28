def divide(dividend: int, divisor: int):
    i = 0
    sign = 1 if divisor > 0 else -1
    sign = sign * 1 if dividend > 0 else sign * -1
    dividend = abs(dividend)
    divisor = abs(divisor)

    if dividend < divisor:
        return 0
    elif divisor == dividend:
        return sign * 1
    else:
        while dividend >= divisor:
            dividend = dividend - divisor
            i += 1

    return i * sign


if __name__ == '__main__':
    print(divide(1, -2))
