test1 = [5, 0, 0]
def tower_of_hanoi(n):
    steps = []
    src = 1
    target = 2
    aux = 3
    hanoi_steps(n, src, target, aux, steps)
    return steps


def hanoi_steps(n, src, dst, aux, steps: []):
    if n == 1:
        steps.append([src, dst])
        return
    else:
        hanoi_steps(n-1, src, aux, dst, steps)
        steps.append([src, dst])
        hanoi_steps(n-1, aux, dst, src, steps)

if __name__ == '__main__':
    print(tower_of_hanoi(4))
