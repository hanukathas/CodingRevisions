def is_valid_sudoku(board: list):
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            if board[i][j] == '.':
                continue
            number = board[i][j]
            box_idx = (i // 3) * 3 + j // 3
            if number in any([row, col, box]):
                return False
            row[i].add(number)
            col[i].add(number)
            box[box_idx].add(number)

    return True
