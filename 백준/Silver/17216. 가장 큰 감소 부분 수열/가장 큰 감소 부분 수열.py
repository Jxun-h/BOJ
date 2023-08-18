from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
dp = [x for x in arr]

for i in range(n):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))