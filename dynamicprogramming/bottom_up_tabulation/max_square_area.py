def max_square_area(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    # print(m, n)
    dp = [[0] * m for _ in range(n)]

    for i in range(m):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]

    max_length = 0
    for i in range(1, m):
        for j in range(1, n):
            # print(i,j, matrix[i][j],dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            if matrix[i][j] != 0:
                if min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) != 0:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    max_length = max(max_length, dp[i][j])
                elif matrix[i-1][j-1] == 1 and matrix[i-1][j] == 1 and matrix[i][j-1] == 1:
                    dp[i][j] = 1
                    max_length = max(max_length, dp[i][j])
    print(max_length)
    return dp

def max_square_area_r(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    # set the table to the breadth * width of the matrix and set the values of the 0th row and column to the matrix values
    # this becomes the table structure and the base case
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]
    max_square = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] != 0:
                if min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) != 0:
                    dp[i][j] = 1 +  min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                elif dp[i-1][j] == 1 and dp[i][j-1] == 1 and dp[i-1][j-1] == 1:
                    dp[i][j] = 1

            max_square = max(max_square, dp[i][j])
    return max_square
if __name__ == '__main__':
    print(max_square_area([[1,1,0],[1,1,1], [1,0,1]]))

