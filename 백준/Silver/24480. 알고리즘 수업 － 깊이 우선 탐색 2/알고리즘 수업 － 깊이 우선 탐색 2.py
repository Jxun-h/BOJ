from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

n, m, r = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
cnt = 1

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(r):
    global cnt
    visited[r] = cnt
    graph[r].sort(reverse=True)
    for node in graph[r]:
        if visited[node] == 0:
            cnt += 1
            dfs(node)


dfs(r)
for i in visited[1:]:
    print(i)
