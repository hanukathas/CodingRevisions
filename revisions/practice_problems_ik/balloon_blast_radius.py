from collections import defaultdict, deque


def balloon_blast_radius(bombs: list):
    n = len(bombs)
    graph = defaultdict(list)

    # Check each pair of bombs
    for i in range(n):
        x1, y1, r1 = bombs[i]
        for j in range(n):
            if i != j:
                x2, y2, r2 = bombs[j]
                # Calculate distance between bombs
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                # If distance is less than radius, i can detonate j
                if distance <= r1:
                    graph[i].append(j)

    def bfs(start):
        visited = {start}
        queue = deque([start])
        while queue:
            curr = queue.popleft()
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited)

    # Try each bomb as starting point
    max_detonated = 0
    for i in range(n):
        max_detonated = max(max_detonated, bfs(i))

    return max_detonated


def find_most_destructive_mine(mines):
    blasted = defaultdict(list)
    n = len(mines)

    for i in range(n):
        x1, y1, r1 = mines[i]
        for j in range(n):
            x2, y2, r2 = mines[j]
            if i != j:
                blast_distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if blast_distance <= r1:
                    blasted[i].append(j)

    def bfs(start):
        visited = {start}
        queue = deque([start])

        while queue:
            mine = queue.popleft()
            for neighbors in blasted[mine]:
                if neighbors not in visited:
                    visited.add(neighbors)
                    queue.append(neighbors)
        return len(visited)

    most_destructive = 0
    for i in range(n):
        most_destructive = max(most_destructive, bfs(i))
    return most_destructive


# Test the function
# mines = [[-3, 3, 3], [-1, 2, 3], [1, 8, 4], [3, 1, 2],
#          [-2, -2, 3.5], [1, 1, 2], [-1, 1, 1], [3, 3, 1]]
# result = find_most_destructive_mine(mines)
# print(result)  # Expected output: [-2, -2, 3.5]

if __name__ == '__main__':
    # mines = [[-3, 3, 3], [-1, 2, 3], [1, 8, 4], [3, 1, 2],
    #          [-2, -2, 3.5], [1, 1, 2], [-1, 1, 1], [3, 3, 1]]
    # result = find_most_destructive_mine(mines)
    # print(result)

    print(find_most_destructive_mine([[2, 1, 3], [6, 1, 4]]))
    print(balloon_blast_radius([[2, 1, 3], [6, 1, 4]]))

    # Test case 2: [[1,1,5],[10,10,5]]
    # assert find_most_destructive_mine([[1, 1, 5], [10, 10, 5]]) == 1

    # Test case 3: [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    # assert find_most_destructive_mine([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]) == 5

    # result = balloon_blast_radius(mines)
    # print(result)