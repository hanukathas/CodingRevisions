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

if __name__ == '__main__':
    print(dfs_traversal(6, [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]))


