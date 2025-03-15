def word_break(words: list, word: str):
    m = len(word)
    dp = [False] * (m+1)
    dp[m] = True

    for i in range (m+1, -1, -1):
        for j in range(i, m+1):
            if word[i:j] in words and dp[j]:
                print(i, j, dp[j])
                dp[i] = True
    print(dp)
    return dp[0]

if __name__ == '__main__':
    print(word_break(['sugar','dad', 'dy'], 'sugardaddy'))