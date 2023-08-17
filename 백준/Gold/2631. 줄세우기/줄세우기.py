from sys import stdin

n = int(stdin.readline())
num = [int(stdin.readline()) for _ in range(n)]

dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j] + 1)

lis = 0
lis = max(lis, max(dp))

answer = n - lis
print(answer)