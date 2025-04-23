from collections import deque, defaultdict


def bfs_traversal(n, edges):
    def bfs_adjacency_list():
        d = defaultdict(list)

        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        return dict(d)

    adjacency = bfs_adjacency_list()
    captured = set()
    print(adjacency)
    captured.add(list(adjacency.keys())[0])


    q = deque()
    q.append(list(adjacency.keys())[0])

    while q:
        v = q.popleft()
        for vertex in adjacency[v]:
            if vertex not in captured:
                captured.add(vertex)
                q.append(vertex)

    return list(captured)

if __name__ == '__main__':
    print(bfs_traversal(6, [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]))












