def max_square_area(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * m for _ in range(n)]

    for i in range(m):
        dp[i][0] = matrix[i][0]
    for j in range(n):
        dp[0][j] = matrix[0][j]
    print(dp)
    max_length = 0
    for i in range(1, m):
        for j in range(1, n):
            print(i,j, matrix[i][j],dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            if matrix[i][j] != 0:
                if min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) != 0:
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    max_length = max(max_length, dp[i][j])
                elif matrix[i-1][j-1] == 1 and matrix[i-1][j] == 1 and matrix[i][j-1] == 1:
                    dp[i][j] = 1
                    max_length = max(max_length, dp[i][j])
    print(max_length)
    return dp

if __name__ == '__main__':
    print(max_square_area([[1,1,1],[0,1,1], [1,1,1]]))

