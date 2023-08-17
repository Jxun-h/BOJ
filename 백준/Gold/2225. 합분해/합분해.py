from sys import stdin


n, k = map(int, stdin.readline().split())
ans = 0
dp = [[0] * 201 for _ in range(201)]
dp[0][:] = [1 for _ in range(201)]
dp[1][:] = [x for x in range(201)]

for i in range(2, 201):
    for j in range(1, 201):
        dp[i][j] = (dp[i][j - 1] + dp[i-1][j]) % 1000000000

print(dp[n][k])