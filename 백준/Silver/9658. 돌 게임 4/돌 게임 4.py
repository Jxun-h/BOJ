from sys import stdin

n = int(stdin.readline())

dp = [0, 0, 1, 0, 1, 1, 1, 1] + [0] * (n - 7)

for i in range(8, n + 1):
    if 0 in [dp[i - 1], dp[i-3], dp[i-4]]:
        dp[i] = 1
    else:
        dp[i] = 0\

print("SK" if dp[n] == 1 else "CY")