def longest_increasing_sequence(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    points = []
    for i in range(m):
        for j in range(n):

            if matrix[i][j] >= matrix[i - 1][j] >= matrix[i][j - 1]:
                dp[i][j] = 1 + max(dp[i][j-1], dp[i-1][j])
                points.append([matrix[i][j], i, j])
            elif matrix[i][j] >= matrix[i - 1][j]:
                dp[i][j] = 1 + dp[i - 1][j]
                points.append([matrix[i][j], i, j])
            elif matrix[i][j] >= matrix[i][j - 1]:
                dp[i][j] = 1 + dp[i][j - 1]
                points.append([matrix[i][j], i, j])
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    print(points)
    print(dp)
    return dp[m-1][n-1] + 1

if __name__ == '__main__':
    print(longest_increasing_sequence( [[3,4,5],[3,2,6],[2,2,1]]))

