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

def set_adjacency():
    adjacency_list = defaultdict(list)
    for edge in matrix:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    return adjacency_list

def graph_bfs(n: int, matrix: list):

    adjacency = set_adjacency()
    traversed = set()

    root = list(adjacency.keys())[0]

    vertexes = deque()
    vertexes.append(root)

    while vertexes:
        edge_vertex = vertexes.popleft()
        traversed.add(edge_vertex)
        for vertex in adjacency[edge_vertex]:
            if not vertex in traversed:
                vertexes.append(vertex)
    return traversed


if __name__ == '__main__':
    matrix = [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]
    print(bfs_traversal(6, matrix))
    print(graph_bfs(6, matrix))












