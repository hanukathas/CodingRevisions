test1 = 0
test2 = 1
test3 = 4
test4 = 30
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_seq(k=2, sum_minus1=1, sum_minus2=0, n=n)

def fibonacci_seq(k, sum_minus1, sum_minus2, n):
    if k > n:
        return sum_minus1
    k_sum = sum_minus1 + sum_minus2
    return fibonacci_seq(k+1, k_sum, sum_minus1, n)


if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(test1))
    print(fibonacci(test2))
    print(fibonacci(test3))
    print(fibonacci(90))
