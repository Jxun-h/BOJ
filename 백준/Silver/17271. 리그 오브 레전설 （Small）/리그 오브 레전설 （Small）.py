from sys import stdin

n, m = map(int, stdin.readline().split())
dp = [0 for _ in range(12500)]
dp[0] = 1
mod = 1000000007

for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    if i - m > -1:
        dp[i] = (dp[i] + dp[i - m]) % mod

print(dp[n])