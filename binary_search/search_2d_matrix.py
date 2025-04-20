def search_2d_matrix(matrix: list, target: int):
    """
        1. here get the total rows and columns of the matrix (m, n)
        2. get the first and last element of the matrix (0, m*n)
        3. calculate the mid as usual. then middle row and middle column are: row / col, row % col
    :param matrix:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])
    start = 0
    end = (m * n) - 1
    while start <= end:
        mid = start + (end - start) // 2
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

if __name__ == '__main__':
    matrix = [
        [1,3,5,7],
        [10,11,16,20],
        [23,30,34,50]
    ]
    target = 3
    print(search_2d_matrix(matrix, target))

