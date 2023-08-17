from sys import stdin

n, m = map(int, stdin.readline().split())
arr = [[0] * (m + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, stdin.readline().split())))

ans = -int(4e9) - 1

psum = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        psum[i][j] = arr[i][j] + psum[i - 1][j]

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp = [0] * (m + 1)
        for k in range(1, m + 1):
            dp[k] = max(psum[j][k] - psum[i - 1][k], dp[k - 1] + psum[j][k] - psum[i - 1][k])
            ans = max(dp[k], ans)
print(ans)
