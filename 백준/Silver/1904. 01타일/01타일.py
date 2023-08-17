from sys import stdin

n = int(stdin.readline())
dp = [0 for _ in range(1000001)]
dp[1], dp[2], dp[3], dp[4] = 1, 2, 3, 5

for i in range(5, n + 1):
    num = ((dp[i-1] + dp[i-2]) % 15746)
    dp[i] = num

print(dp[n])