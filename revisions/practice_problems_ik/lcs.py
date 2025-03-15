def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    wdp = [[""] * (n + 1) for _ in range(m + 1)]

    # Fill dp table same as before
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                wdp[i][j] = wdp[i-1][j-1] + a[i-1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if dp[i - 1][j] > dp[i][j - 1]:
                    wdp[i][j] = wdp[i - 1][j]
                else:
                    wdp[i][j] = wdp[i][j - 1]
    if wdp[m][n] != "":
        return wdp[m][n], dp[m][n]
    else:
        return "-1"




if __name__ == '__main__':
    print(lcs("AAAAAA",
              "AAAAAABBBBBB"))
