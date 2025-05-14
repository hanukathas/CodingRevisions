def board_game(moves: list, board_size: int):
    board = {}
    current_player = 1
    def is_valid(x, y):
        return 0 <= x <= board_size and 0 <= y <= board_size

    def toggle_move(x, y, direction):
        new_x = x
        new_y = y
        if direction == 'u': new_x = x - 1
        elif direction == 'd': new_x = x + 1
        elif direction == 'l':
            new_y = y - 1
        elif direction == 'r':
            new_y = y + 1

        if is_valid(new_x, new_y):
            pieces = board[(x, y)]
            if len(pieces) == 0:
                return
            del board[(x, y)]

            existing_pieces = board.get((new_x, new_y), [])
            board[(new_x, new_y)] = pieces

    for move in moves:
        if move[0] == 'p':
            x, y = move[1], move[2]
            if is_valid(x, y):
                pos = (x,y)
                board[pos] = board.get(pos, []) + [current_player]
                current_player = 3 - current_player
        if move[0] == 'd':
            x, y = move[1], move[2]
            if is_valid(x, y):
                direction = move[3]
                toggle_move(x, y, direction)

    


