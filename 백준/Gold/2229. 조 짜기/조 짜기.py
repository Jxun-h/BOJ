from sys import stdin

n = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]

for i in range(1, n):
    for j in range(1, i + 2):
        temp = data[i - j + 1:i + 1]
        if j == i + 1:
            j = i
        dp[i] = max(dp[i], dp[i-j] + abs(max(temp) - min(temp)))

print(dp[-1])
