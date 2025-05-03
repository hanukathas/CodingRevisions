from collections import deque


def is_component_bipartite(matrix: list):
    """
    https://leetcode.com/problems/is-graph-bipartite/
    :return:
    """
    n = len(matrix)
    adjacency_list = {}
    parent = [-1] * n
    level = [-1] * n
    visited = []
    for i in range(n):
        adjacency_list[i] = matrix[i]

    # bfs set up
    # do this in a loop if there are more than one connected components
    # for each connected component, we can just call this function and the adjacency matrix
    # the vertexes from the origin wont collide

    queue = deque()
    origin = list(adjacency_list.keys())[0]
    queue.append(origin)
    level[origin] = 0
    visited.append(origin)

    while queue:
        vertex = queue.popleft()

        for end_vertex in adjacency_list[vertex]:
            print(visited)
            if end_vertex not in visited:
                visited.append(end_vertex)
                parent[end_vertex] = vertex
                level[end_vertex] = 1 + level[vertex]
                queue.append(end_vertex)
            else:
                print(end_vertex, vertex, level)
                if level[end_vertex] == level[vertex]:
                    return False

    return True


if __name__ == '__main__':
    print(is_component_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
    print(is_component_bipartite([[1,3],[0,2],[1,3],[0,2]]))