from collections import defaultdict

def dfs_traversal(n, edges):
    def bfs_adjacency_list():
        d = defaultdict(list)

        for edge in edges:
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
        return dict(d)

    adjacency = bfs_adjacency_list()
    print(adjacency)

    root = list(adjacency.keys())[0]
    visited = {}

    def dfs(root):
        visited[root] = 1

        for vertex in adjacency[root]:
            if vertex not in visited:
                dfs(vertex)
    dfs(root)
    return list(visited.keys())

def graf_dfs(n: int, matrix: list):
    def set_adjacency():
        adjacency_list = defaultdict(list)
        for edge in matrix:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        return adjacency_list
    adjacency = set_adjacency()

    traversed = set()

    root = list(adjacency.keys())[0]

    def dfs(root: int, traversed_set: set):
        traversed_set.add(root)
        for vertex in adjacency[root]:
            if vertex not in traversed:
                dfs(vertex, traversed_set)

    dfs(root, traversed)

    return traversed


if __name__ == '__main__':
    matrix = [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]
    print(dfs_traversal(6, matrix))
    print(graf_dfs(6, matrix))


