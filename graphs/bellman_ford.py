def bellman_ford(graph: dict, start: str):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    previous = {vertex: None for vertex in graph}

    edges = [[u,v,w] for u in graph for v,w in graph[u].items()]
    n = len(edges)

    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                previous[v] = u

    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("graph contains negative edges")

    return  distances, previous

if __name__ == '__main__':
    graph = {
        'A': {'B': -1, 'C': 4},
        'B': {'C': 3, 'D': 2},
        'C': {'D': -5},
        'D': {},
    }

    try:
        distances, previous = bellman_ford(graph, 'A')
        print("Distances from A:", distances)
    except ValueError as e:
        print(e)