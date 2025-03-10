def factorial(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(2, n+1):
            fact = fact * i
    return fact

if __name__ == '__main__':
    print(factorial(4))
