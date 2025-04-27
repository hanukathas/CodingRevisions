def robots_move(instructions: str):
    def move(x, y, d, i):
        if i == 'R':
            d = (d + 1) % 4
            return x,y,d
        elif i == 'L':
            d = (d - 1) % 4
            return x, y, d
        else:
            if d == 0:
                y += 1
            if d == 1:
                x += 1
            if d == 2:
                y -= 1
            if d == 3:
                x -= 1
            return x, y, d

    start = 0
    end = 0
    dir = 0
    for i in instructions:
        start, end, dir = move(start, end, dir, i)

    if (start,end) != 0 and dir == 0:
        return False
    else:
        return True

def robots_move_r(instructions: str):
    D = 0
    X = 0
    Y = 0
    def move(ch, x, y, d):
        if ch == 'L':
            return (d - 1) % 4, x, y
        elif ch == 'R':
            return (d + 1) % 4, x, y
        else:
            if d == 0:
                return d, x + 1, y
            if d == 1:
                return d, x, y + 1
            if d == 2:
                return d, x - 1, y
            if d == 3:
                return d, x, y - 1


    for i in range(len(instructions)):
        D, X, Y = move(instructions[i], X, Y, D)

    if (X, Y) != 0 and D == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(robots_move("GL"))
    print(robots_move("GG"))

    print(robots_move_r("GL"))
    print(robots_move_r("GG"))