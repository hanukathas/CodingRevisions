def factorial(n):
    mem = {}
    mem[0] = 1
    mem[1] = 1
    return fact(n, mem)

def fact(n: int, mem: dict) -> int:
    if n in mem:
        return mem[n]
    else:
        mem[n] = n * fact(n-1, mem)
        return mem[n]

if __name__ == '__main__':
   print(factorial(5))