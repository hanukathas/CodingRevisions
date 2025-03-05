test1 = 0
test2 = 1
test3 = 5
def factorial(n):
    if n < 0:
        return -1

    elif n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    print(factorial(test1))
    print(factorial(test2))
    print(factorial(test3))
    print(factorial(-4))