from sys import stdin

n = int(stdin.readline())
dp = [0 for _ in range(100001)]
dp[1], dp[2], dp[3] = 3, 7, 17

for i in range(4, 100001):
    dp[i] = (dp[i - 1] * 2 + dp[i - 2]) % 9901

print(dp[n])