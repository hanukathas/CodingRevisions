from collections import deque
from multiprocessing.connection import answer_challenge


def get_neighbors(cell: list):
    return [(cell[0]-1, cell[1]), (cell[0]+1, cell[1]), (cell[0], cell[1] + 1), (cell[0], cell[1] - 1)]

def can_visit(row, col, R, C, grid: list, visited: list):
    if row < 0 or row >= R:
        return False
    if col < 0 or col >= C:
        return False
    if visited[row][col]:
        return False
    if grid[row][col] == 0:
        return False
    return True

def bfs(row, col, R, C, grid, visited):
    queue = deque()
    visited[row][col] = True
    queue.append([row, col])
    count = 0

    while queue:
        vertex = queue.popleft()
        count += 1
        for neighbor in get_neighbors(vertex):
            if can_visit(neighbor[0], neighbor[1], R, C, grid, visited):
                queue.append(neighbor)
                visited[neighbor[0]][neighbor[1]] = True
    return count


def count_islands(grid: list):
    """
    https://leetcode.com/problems/number-of-islands/description/
    Logic:
    1. get can visit: check from the current row and column and compare it against visited and grid
        can't visit further if its already visited and/or grid value is 0
    2. get the neighbors: left, right, up, down
    3. navigate for every vertex and check their neighbors and move along
    https://uplevel.interviewkickstart.com/resource/rc-codingproblem-1085630-2182813-250-1590
    :param matrix:
    :return:
    """
    R = len(grid)
    C = len(grid[0])
    visited = [[False] * C for _ in range(R)]
    max_islands = 0

    for row in range(R):
        for col in range(C):
            if can_visit(row, col, R, C, grid, visited):
                islands = bfs(row, col, R, C, grid, visited)
                max_islands = max(max_islands, islands)
    return max_islands












