from collections import deque, defaultdict


def connected_components(n: int, edges: list):
    """
    structure:
    1. build the adjacency list or adjacency map
    2. decide between BFS and DFS
    3. within BFS or DFS, compute the results and base cases etc.
    4. external control

    For this problem:
    1. we can build the adjacency list
    2. use BFS to know get the visited list
    3. for a given source root, if not all vertices are not visited, increase components by 1 and recurse
    :param n:
    :param edges:
    :return:
    """
    adj_list = [[] for _ in range(n)]

    # Creating adjacency list representation
    for edge in edges:
        u, v = edge
        adj_list[u].append(v)
        adj_list[v].append(u)

    number_of_components = 0
    visited = [False] * n

    for node_value in range(n):
        if not visited[node_value]:
            number_of_components += 1
            visited[node_value] = True
            nodes = deque([node_value])

            # Below while loop will set visited[x] = True for every node x which is
            # reachable from the node_value.
            while nodes:
                current_node = nodes.popleft()

                # Visiting all the neighbor nodes of current_node.
                for connected_node in adj_list[current_node]:
                    if not visited[connected_node]:
                        visited[connected_node] = True
                        nodes.append(connected_node)

    return number_of_components

def set_adjacency(matrix):
    adjacency_list = defaultdict(list)
    for edge in matrix:
        adjacency_list[edge[0]].append(edge[1])
        adjacency_list[edge[1]].append(edge[0])

    return adjacency_list

def bfs_traversal(adjacency: {}, traversed: set, root: int):
    vertexes = deque()
    vertexes.append(root)

    while vertexes:
        edge_vertex = vertexes.popleft()
        traversed.add(edge_vertex)
        for vertex in adjacency[edge_vertex]:
            if not vertex in traversed:
                vertexes.append(vertex)
    return traversed

def cc(n:int, matrix: list):
    adjacency = set_adjacency(matrix=matrix)
    traversed = set()
    unconnected_components = 0
    for i in range(n):
        if i not in traversed:
            print(i)
            unconnected_components += 1
            traversed = bfs_traversal(adjacency=adjacency, traversed=traversed, root=i)

    return unconnected_components

if __name__ == '__main__':
    matrix = [
[0, 1],
[0, 2],
[0, 4],
[2, 3]
]
    print(cc(6, matrix))
