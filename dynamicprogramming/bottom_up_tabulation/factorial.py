def factorial(n):
    result = 1
    i = 2
    while i <= n:
        result = result * i
        i += 1
    return result

if __name__ == '__main__':
    print(factorial(5))
