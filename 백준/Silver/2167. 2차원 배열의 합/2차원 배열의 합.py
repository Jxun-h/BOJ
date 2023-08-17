from sys import stdin

n, m = map(int, stdin.readline().strip().split())
arr = []

for _ in range(n):
    arr.append(list(map(int, stdin.readline().strip().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = arr[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]

for _ in range(int(stdin.readline().strip())):
    i, j, x, y = map(int, stdin.readline().strip().split())
    print(dp[x][y] - dp[x][j - 1] - dp[i - 1][y] + dp[i - 1][j - 1])