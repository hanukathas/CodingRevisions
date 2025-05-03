from collections import deque


def snake_ladder(n, moves):
    visited = [False for _ in range(n)]
    start = [0,0] # current position, # of moves to this position
    queue = deque()
    queue.append(start)

    while queue:
        position = queue.popleft()
        if visited[position[0]]:
            continue
        visited[position[0]] = True

        if position[0] == n - 1:
            return position[1]


        for i in range(1, 7):
            next_position = position[0] + i
            if next_position >= n: # you have crossed the boundar
                break

            ladder = moves[next_position]
            if ladder != -1:
                next_position = ladder

            queue.append([next_position, position[1] + 1])
    return -1

