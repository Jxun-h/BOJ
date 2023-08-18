from sys import stdin

dp = [0 for _ in range(120)]
dp[0:3] = [1, 1, 1, 2]

for x in range(4, 117):
    dp[x] = (dp[x - 3] + dp[x - 1])

print(dp[int(stdin.readline()) - 1])