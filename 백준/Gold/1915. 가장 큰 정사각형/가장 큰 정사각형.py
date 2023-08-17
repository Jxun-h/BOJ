from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, list(stdin.readline().rstrip()))))

ans = 0
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if arr[i - 1][j - 1] == 1:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
            ans = max(ans, dp[i][j])

print(ans ** 2)
