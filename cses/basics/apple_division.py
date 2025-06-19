#works 
def apple_division(n: int, apples: list):
    if n == 1:
        return apples[0]
    if n == 2:
        return abs(apples[0] - apples[1])

    def divide(idx, sum1, sum2):
        if idx == n:
            return abs(sum2 - sum1)

        choose = divide(idx + 1, sum1 + apples[idx], sum2)
        not_choose = divide(idx + 1, sum1, sum2 + apples[idx])

        return min(choose, not_choose)

    return divide(0, 0, 0)

