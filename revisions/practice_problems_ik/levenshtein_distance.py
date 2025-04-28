def levenshtein_distance2(word1, word2):
    # instantiate a space to an array whose size matches the cartesian product of the length of the two words
    """
    https://leetcode.com/problems/edit-distance/description/
    :param word1:
    :param word2:
    :return:
    """
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1)+1)]
    m = len(word1)
    n = len(word2)
    # base case: the other word is an empty string
    for i in range(m+1):
        dp[i][0] = i
    for i in range(n+1):
        dp[0][i] = i
    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]


def levenshtein_distance(word1, word2):
    # Create a matrix of size (m+1) x (n+1) where m and n are lengths of words
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting characters from word1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting characters from word2

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # If characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j],  # deletion
                    dp[i][j - 1],  # insertion
                    dp[i - 1][j - 1]  # replacement
                )

    return dp[m][n]



if __name__ == '__main__':
    print(levenshtein_distance2('cat', 'bacatt'))