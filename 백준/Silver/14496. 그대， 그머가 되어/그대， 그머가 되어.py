from collections import deque
from sys import stdin

a, b = map(int, stdin.readline().split())
n, m = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)


def bfs(start, end):
    q = deque()
    visited = [0 for _ in range(n + 1)]
    q.append((start, 0))

    while q:
        now, cost = q.popleft()

        if now == end:
            return cost

        for node in graph[now]:
            if not visited[node]:
                q.append((node, cost + 1))
                visited[node] = 1

    return -1


print(bfs(a, b))