from sys import stdin, setrecursionlimit

setrecursionlimit(100 ** 3)

arr = [[0, 0]]
n, limit = map(int, stdin.readline().split())
for i in range(n):
    arr.append(list(map(int, stdin.readline().split())))

dp = [[0] * (limit + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, limit + 1):
        use_time, point = arr[i]

        if j < use_time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - use_time] + point)

print(dp[n][limit])
