def search_matrix(arr: list, target: int):
    row = 0
    col = len(arr[0]) -1
    print(row, col)
    while row < len(arr) and col > -1:
        if target == arr[row][col]:
            return True
        elif target < arr[row][col]:
            col -= 1
            print(row, col)
        else:
            row += 1

            print(row, col)
    return False

def search_matrix_revision(arr: list, target: int):
    row = 0
    col = len(arr[0]) - 1
    while row < len(arr) and col > -1:
        if target == arr[row][col]:
            return True
        elif target < arr[row][col]:
            col -= 1
        else:
            row += 1
    return None


if __name__ == '__main__':
    print(search_matrix([[1,4,10], [2,5,12],[3,6,14]], 50))
    print(search_matrix([[1, 4, 10], [2, 5, 12], [3, 6, 14]], 5))

