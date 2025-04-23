def convert_edge_list_to_adjacency_matrix(n, edges):
    adjacency_matrix = [[0] * n for _ in range(n)]
    for edge in edges:
        
        adjacency_matrix[edge[0]][edge[1]] = 1
        adjacency_matrix[edge[1]][edge[0]] = 1

    return adjacency_matrix


if __name__ == '__main__':
    print(convert_edge_list_to_adjacency_matrix(5, [
        [0, 1],
        [1, 4],
        [1, 2],
        [1, 3],
        [3, 4]
    ]))
