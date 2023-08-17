from sys import stdin

n, m = map(int, stdin.readline().split())
inf = int(1e9)
graph = [[inf] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if j == k:
                graph[j][k] = 0
                continue
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]


res = n
for i in range(1, n + 1):
    checker = 1
    for j in range(1, n + 1):
        if graph[i][j] == inf and graph[j][i] == inf:
            res -= 1
            checker = 0
        if not checker:
            break

print(res)