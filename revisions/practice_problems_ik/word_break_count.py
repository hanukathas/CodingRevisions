def word_break_count(dictionary, txt):
    m = len(txt)
    dp = [0] * (m+1)
    dp[m] = 1
    mod = int(1e9) + 7

    word_set = set(dictionary)
    print(word_set)

    for i in range (m+1, -1, -1):
        for j in range(i, m+1):
            if txt[i:j] in word_set:
                print(txt[i:j])
                dp[i] = (dp[i] + dp[j]) % mod

    return dp[0]




if __name__ == '__main__':
    # print(word_break_count(["kick", "start", "kickstart", "is", "awe", "some", "awesome"], 'kickstartisawesome'))
    # print(word_break_count(["my", "name", "myname", "nameis", "is", "mynameis", "karthik"], "mynameiskarthik"))
    # print(word_break_count(["world", "hello", "faang"], "helloworldhello"))
    # print(word_break_count(["interview", "preparation"], "interviewkickstart"))
    print(word_break_count(["world", "hello", "faang"], "helloworldhello"))