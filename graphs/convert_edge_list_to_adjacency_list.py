from collections import defaultdict


def convert_edge_list_to_adjacency_list(n, edges):
    d = defaultdict(list)
    for edge in edges:
        d[edge[0]].append(edge[1])
        d[edge[1]].append(edge[0])

    return list(d.values())


if __name__ == '__main__':
    print(convert_edge_list_to_adjacency_list(5, [
        [0, 1],
        [1, 4],
        [1, 2],
        [1, 3],
        [3, 4]
    ]))
