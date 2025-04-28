def word_break(words: list, word: str):
    m = len(word)
    dp = [False] * (m+1)
    dp[m] = True

    for i in range (m+1, -1, -1):
        for j in range(i, m+1):
            if word[i:j] in words and dp[j]:

                dp[i] = True
    print(dp)
    return dp[0]

def word_break_r(words: list, word: str):
    n = len(word)
    dp = [False] * (n + 1)
    dp[n] = True

    for i in range(n-1, -1, -1):
        for j in range(i, n-1):
            if word[i:j] in words and dp[j]:
                dp[i] = True
    return dp[0]




def word_break_revision(words: list, word: str):
    """
        if the word is empty then return 0
        the table for a given letter in the word is the total number of ways
        from that letter -
    :param words:
    :param word:
    :return:
    """
    n = len(word)
    dp = [0] * (len(word)+1)
    dp[n] = 1
    word_set = set(words)
    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1):
            if word[i:j] in word_set:
                dp[i] = dp[i] + dp[j]
    print(dp)
    return dp[0]



if __name__ == '__main__':
    print(word_break(['sugar','dad', 'dy'], 'sugardaddy'))
    print(word_break_revision(['sugar', 'dad', 'dy'], 'sugardaddy'))