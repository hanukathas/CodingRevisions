import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]
    previous = {node: None for node in graph}

    while pq:
        curr_distance, curr_vertex = heapq.heappop(pq)
        if curr_distance > distances[curr_vertex]:
            continue

        for neighbor, weight in graph[curr_vertex].items():
            distance = weight + curr_distance # weight + actual distance
            if distance < distances[neighbor]: #
                distances[neighbor] = distance
                previous[neighbor] = curr_vertex
                heapq.heappush(pq, (distance, neighbor))
    return distances, previous

def get_shortest_path(previous: dict, start: str, end: str):
    path = []
    curr = end
    path.append(curr)
    while curr:
        path.append(previous[curr])
        curr = previous[curr]
    return path[:-1]






if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }

    start_vertex = 'A'
    distances, previous = dijkstra(graph, start_vertex)
    print(f"Distances from {start_vertex}:", distances)


    # Get path from A to E
    path = get_shortest_path(previous, 'A', 'E')
    print(path)
    print("Shortest path from A to E:", ' -> '.join(path))
