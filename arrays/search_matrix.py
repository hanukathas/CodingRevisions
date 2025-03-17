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

if __name__ == '__main__':
    print(search_matrix([[1,4,10], [2,5,12],[3,6,14]], 50))

