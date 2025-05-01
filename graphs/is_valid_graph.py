from collections import defaultdict, deque


def is_valid_graph(n: int, edges: list):
    """
    1. component count = 1. A single queue loop visits all vertexes
    2. at least one vertex has odd edges
    
    :param n:
    :param edges:
    :return:
    """
    traversed = set()
    parent = [-1] * n
    def set_adjacency_list():
        a_list = defaultdict(list)
        for edge in edges:
            a_list[edge[0]].append(edge[1])
            a_list[edge[1]].append(edge[0])

        return a_list
    adjacency_list = set_adjacency_list()

    queue = deque()
    origin = list(adjacency_list.keys())[0]
    queue.append(origin)
    # traversed.add(origin)
    # parent[origin] = origin


    while queue:
        vertex = queue.popleft()
        # traversed.add(vertex)
        for vertex_end in adjacency_list[vertex]:

            if vertex_end not in traversed:
                traversed.add(vertex_end)
                parent[vertex_end] = vertex
                queue.append(vertex_end)
            else:
                if parent[vertex] != vertex_end:
                    return False

    return set(i for i in range(n)) == traversed

if __name__ == '__main__':
#     print(is_valid_graph(5, [
# [0, 1],
# [0, 2],
# [1, 3],
# [3, 0],
# [3, 2],
# [4, 3],
# [4, 0]
# ]))

    print(is_valid_graph(3, [
        [0,1], [1,2]
    ]))








