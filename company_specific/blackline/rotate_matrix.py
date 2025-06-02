from os import PRIO_PGRP


def rotate_matrix(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print("\n")
    for row in matrix:
        print(row)


    return matrix

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Original matrix:")
    for row in matrix:
        print(row)

    rotate_matrix(matrix)
    print("\nRotated matrix:")
    for row in matrix:
        print(row)

