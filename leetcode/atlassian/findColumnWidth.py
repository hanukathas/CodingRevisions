def findColumnWidth(grid: list[list[int]]) :
    """
        problem link: https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/?envType=company&envId=atlassian&favoriteSlug=atlassian-six-months
        algo:
        1. get row size and assign to row
        2. get column size and assign to col
        3. look through rows and columns, keep the max col size
        4. add it to ans once the loop is completed
        5. catch: since len cannot be applied to char (gets the ASCII value), use str
    :param self:
    :param grid:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])
    print(rows, cols)
    ans = []
    ans2 = []
    for i in range(rows):
        max_val = 0
        for j in range(cols):
            print(i, j, grid[i][j])
            max_val = max(max_val, len(str(grid[i][j])))
        ans.append(max_val)
    for j in range(cols):
        max_val = 0
        for i in range(rows):
            print(i, j, grid[i][j])
            max_val = max(max_val, len(str(grid[i][j])))
        ans2.append(max_val)
    return ans, ans2

if __name__ == '__main__':
    print(findColumnWidth([[1],[22],[333]]))
    print(findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]]))
    print(findColumnWidth([[-15, 2, 3]] ))
    
