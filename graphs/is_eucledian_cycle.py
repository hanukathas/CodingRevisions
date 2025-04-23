def is_eucledian_cycle(n: int, edges: list):
    degrees = [0] * n
    for edge in edges:
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    return all(degree % 2 == 0 for degree in degrees)

if __name__ == '__main__':
    print(is_eucledian_cycle(5, [
[0, 1],
[0, 2],
[1, 3],
[3, 0],
[3, 2],
[4, 3],
[4, 0]
]))