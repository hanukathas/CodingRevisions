from collections import deque


def count_islands(matrix: list):
    islands = 0
    m = len(matrix)
    n = len(matrix[0])

    adj_r = [0, -1, -1, -1, 0, 1, 1, 1]
    adj_c = [-1, -1, 0, 1, 1, 1, 0, -1]

    def island_bfs(x, y):
        matrix[x][y] = 0
        queue = deque([x,y])

        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(8):
                new_x = cur_x + adj_r[i]
                new_y = cur_y + adj_c[i]
                if new_x < 0 or new_y < 0 or new_y >= n or new_x >= m:
                    continue
                if matrix[new_x][new_y] == 1:
                    queue.append((new_x,new_y))
                    matrix[new_x][new_y] = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                islands += 1
                island_bfs(i, j)
    return islands