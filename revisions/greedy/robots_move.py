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

if __name__ == '__main__':
    print(robots_move("GG"))