from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
dp = [0 for _ in range(n + 1)]

for i in range(m):
    for j in range(n, 0, -1):
        if arr[i][0] <= j:
            dp[j] = max(dp[j], dp[j - arr[i][0]] + arr[i][1])

print(dp[n])