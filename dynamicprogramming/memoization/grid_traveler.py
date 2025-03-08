def grid_traveler(m: int,n: int, mem: dict) -> int:
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    key = f"{m},{n}"
    if key in mem:
        return mem[key]

    mem[key] = grid_traveler(m-1, n, mem) + grid_traveler(m,n-1, mem)
    return mem[key]


if __name__ == '__main__':
    print(grid_traveler(2,3,{}))
