def robot_move(moves: str):
    """
    at the end of a single simulation if we face North and have moved then we make magnitudal change
    :param moves:
    :return:
    """
    x_point = y_point = 0
    direction = 0
    def simulate(x, y, d, i):
        if i == 'L':
            return x, y, (d - 1) % 4
        if i == 'R':
            return x, y, (d + 1) % 4
        else:
            if d == 0:
                return x, y + 1, d
            if d == 1:
                return x + 1, y, d
            if d == 2:
                return x, y - 1, d
            if d == 3:
                return x - 1, y, d
            return None

    for i in moves:
        x_point, y_point, direction = simulate(x_point, y_point, direction, i)
    print(x_point, y_point, direction)
    if (x_point, y_point) != (0,0) and direction == 0:
        return False
    else:
        return True

def robot_move_r(moves: str):
    x, y, dir = 0, 0, 0

    def curr_position(x, y, d, move):
        if move == 'R':
            return x, y, (d + 1) % 4
        elif move == 'L':
            return x, y, (d - 1) % 4
        else:
            if d == 0:
                return x , y + 1, d
            elif d == 2:
                return x, y - 1, d
            elif d == 1:
                return x + 1, y, d
            else:
                return x - 1, y, d

    for i in moves:
        x, y, dir = curr_position(x, y, dir, i)
    print(x, y, dir)
    if (x, y) != (0, 0) and dir == 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print(robot_move_r('LL'))




