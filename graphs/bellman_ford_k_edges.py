def bellman_ford_k_edges(graph: {}, start: str, k: int):
    edges = [[u,v,w] for u in graph for v, w in graph[u].items()]
    n = len(edges)
    distances = [[float('inf')] * (k + 2) for _ in range(n)]
    distances[0][0] = 0

    for col in range(1, k+2):
        for row in range(n):
            distances[row][col] = distances[row][col - 1]
            for u, v, w in edges:
                distances[v][col] = min(distances[v][col], distances[u][col-1] + w)


    return distances[k][k+1]

if __name__ == '__main__':
    graph = {
        0: {1: -1, 2: 4},
        1: {2: 3, 3: 2},
        2: {3: -5},
        3: {}
    }

    # Find shortest paths from 'A' using exactly 2 edges
    k = 2
    distances = bellman_ford_k_edges(graph, 'A', k)
    print(f"Shortest distances from A using exactly {k} edges:", distances)
