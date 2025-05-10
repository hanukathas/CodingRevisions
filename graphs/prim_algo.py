import heapq


def prim_algo(graph, start):
    mst = []
    visited = {start}
    edges = [(weight, start, to) for to, weight in graph[start].items()]

    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)

        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            # Add new edges to priority queue
            for next_node, next_weight in graph[to].items():
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, to, next_node))

    return mst
def prims(start: str, graph: dict):
    mst = [] # minimum spanning tree, output
    visited = {start}
    edges = [(weight, start, end) for end, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        w, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((w, frm, to))

            for neighbor_to, neighbor_weight in graph[to].items():
                if neighbor_to not in visited:
                    heapq.heappush(edges, (neighbor_weight, to, neighbor_to))
    return mst

if __name__ == '__main__':
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }

    minimum_spanning_tree = prim_algo(graph, 'A')
    print("Minimum Spanning Tree:", minimum_spanning_tree)