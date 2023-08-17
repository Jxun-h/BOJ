from sys import stdin

n = int(stdin.readline())
dp = [0] * (n + 1)
g = {}

for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))
    dp[i] = data[0]

    if data[1] == 0:
        continue
    for j in data[2:]:
        if i in g:
            g[i].append(j)
        else:
            g[i] = [j]

for i in range(1, n + 1):
    if i in g:
        time = 0
        for j in g[i]:
            time = max(time, dp[j])
        dp[i] += time

print(max(dp))