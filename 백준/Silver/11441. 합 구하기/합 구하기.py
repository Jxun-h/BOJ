from sys import stdin

n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

dp = [0 for _ in range(n)]
dp[0], dp[1] = arr[0], sum(arr[:2])

for i in range(2, n):
    dp[i] = dp[i - 1] + arr[i]


m = int(stdin.readline().strip())

for _ in range(m):
    x, y = map(int, stdin.readline().split())

    if x == 1:
        print(dp[y - 1])
    else:
        print(dp[y - 1] - dp[x - 2])