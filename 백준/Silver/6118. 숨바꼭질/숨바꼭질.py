from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

res = [[] for _ in range(20001)]
max_dist = -1e9


def bfs(n):
    global max_dist
    q = deque()
    q.append((0, n))
    visited = set()
    visited.add(n)

    while q:
        dist, now = q.popleft()
        max_dist = max(max_dist, dist)
        for node in arr[now]:
            if node not in visited:
                visited.add(node)
                q.append((dist + 1, node))
                res[dist + 1].append(node)


bfs(1)
print(min(res[max_dist]), max_dist, len(res[max_dist]))