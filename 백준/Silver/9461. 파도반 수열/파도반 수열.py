from sys import stdin

dp = [0 for _ in range(101)]
dp[0], dp[1], dp[2] = 1, 1, 1

for i in range(3, 101):
    dp[i] = dp[i - 3] + dp[i - 2]

for _ in range(int(stdin.readline())):
    print(dp[int(stdin.readline()) - 1])