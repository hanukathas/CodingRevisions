test1 = 0
test2 = 1
test3 = 5
test4 = 30

def fibonacci_series(n: int):
    mem = {}
    mem[0] = 0
    mem[1] = 1
    return fib(n, mem)

def fib(n: int, mem: dict) -> int:
    if n in mem:
        return mem[n]
    else:
        mem[n] = fib(n-1, mem) + fib(n-2, mem)
        return mem[n]
if __name__ == '__main__':
    print(fibonacci_series(3))