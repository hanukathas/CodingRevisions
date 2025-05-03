from collections import deque


add_r = [0, -1, -1, -1, 0, 1, 1, 1]
add_c = [-1, -1, 0, 1, 1, 1, 0, -1]

def islands_bfs(row, col, matrix):
    matrix[row][col] = 0
    queue = deque()
    queue.append((row, col))

    while queue:
        cur_row, cur_col = queue.popleft()
        for i in range(8):
            new_row = cur_row + add_r[i]
            new_col = cur_col + add_c[i]

            if new_col < 0 or new_row < 0 or new_row >= len(matrix) or new_col >= len(matrix[0]):
                continue
            if matrix[new_row][new_col] != 0:
                queue.append((new_row, new_col))
                matrix[new_row][new_col] = 0




def count_islands(matrix: list):
    total_rows = len(matrix)
    total_columns = len(matrix[0])
    islands = 0
    for i in range(total_rows):
        for j in range(total_columns):
            if matrix[i][j] != 0:
                islands += 1
                islands_bfs(i, j, matrix)
    return islands