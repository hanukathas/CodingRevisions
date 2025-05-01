def is_eucledian_path(n: int, edges: list):
    degrees = [0] * n
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    count = 0
    for i in degrees:
        if i % 2 == 1:
            count += 1
            if count > 2:
                return False

    return True

def is_path(n: int, matrix: []):
    degrees = [0] * n
    for edges in matrix:
        degrees[edges[0]] += 1
        degrees[edges[1]] += 1

    odd_degrees_count = 0

    for degree in degrees:
        if degree % 2 != 0:
            odd_degrees_count += 1

    return odd_degrees_count <= 2


if __name__ == '__main__':
    print(is_eucledian_path(5, [
[0, 3],
[1, 2],
[1, 3],
[3, 2],
[4, 1],
[4, 2]
]))

