
n, x = map(int, input().split())
h = list(map(int, input().split()))
s = list(map(int, input().split()))

dp = [0] * (x + 1)
for i in range(n):
    for j in range(x, h[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - h[i]] + s[i])

print(dp[x])