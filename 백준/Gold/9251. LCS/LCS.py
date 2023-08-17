from sys import stdin

s1 = list(stdin.readline().rstrip())
s2 = list(stdin.readline().rstrip())
n = len(s1)
m = len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]


for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

print(dp[m][n])