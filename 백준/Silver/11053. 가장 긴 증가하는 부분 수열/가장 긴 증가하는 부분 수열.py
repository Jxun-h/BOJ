from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = 1
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
