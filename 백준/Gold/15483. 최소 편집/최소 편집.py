from sys import stdin
s1 = list(stdin.readline().strip().rstrip())
s2 = list(stdin.readline().strip().rstrip())
n, m = len(s1), len(s2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    dp[i][0] = i

for i in range(1, n + 1):
    dp[0][i] = i

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[j - 1] == s2[i - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

print(dp[m][n])
