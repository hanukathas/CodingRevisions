def lcs_bottom_up_copy(str1, str2):

    lcs = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]

    for m in range(1, len(str1)+1):
        for n in range(1, len(str2)+1):
            if str1[m-1] == str2[n-1]:
                lcs[m][n] = lcs[m-1][n-1] + 1
            else:
                lcs[m][n] = max(lcs[m-1][n],lcs[m][n-1])
    return lcs[len(str1)][len(str2)]


def lcs_bottom_up(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def lcs_bottom_up_revision(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def lcs_bottom_up_revision_2(str1, str2):
    """
    first step is to set up the table
    second step is the base condition
    third is the calculation for m, n when m-1, n-1 are calculated
    loops always for the next element, looking at the prev element
    :param str1:
    :param str2:
    :return:
    """
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #which ever has a higher match coefficient
    return dp[m][n]


if __name__ == '__main__':
    # print(lcs_bottom_up("hello", "ell"))
    print(lcs_bottom_up_copy("leetcode", "cod"))
    print(lcs_bottom_up_revision_2("beautybb", "b"))

