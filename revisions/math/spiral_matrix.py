def spiral_matrix(n:int):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right = 0, n-1
    top, bottom = 0, n-1
    while num <= n**2:
        # fill top
        for i in range(left, right + 1):
            print(num)
            matrix[top][i] = num
            num += 1
        top += 1

        # fill right
        for i in range(top, bottom + 1):
            print(num)
            matrix[i][right] = num
            num += 1
        right -= 1

        # fill bottom
        for i in range(bottom, left - 1, -1):
            print(num)
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # fill left
        for i in range(bottom, top - 1, -1):
            print(num)
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix

if __name__ == '__main__':
    print(spiral_matrix(4))


