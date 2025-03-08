def climbing_stairs(n, mem:{}) -> int:
    if n <= 2:
        return n
    elif n in mem:
        return mem[n]
    else:
        mem[n] = climbing_stairs(n-1, mem) + climbing_stairs(n-2, mem)
        return mem[n]

if __name__=='__main__':
    print(climbing_stairs(4,{}))