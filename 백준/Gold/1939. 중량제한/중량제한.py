from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, stdin.readline().split())
l, r = 0, int(1e9)


def solve(mid):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        if now == end:
            return True

        for node, cost in graph[now]:
            if not visited[node] and mid <= cost:
                q.append(node)
                visited[node] = True

    return False


ans = 0
while l <= r:
    mid = (l + r) // 2
    visited = [False for _ in range(n + 1)]

    if solve(mid):
        ans = max(ans, mid)
        l = mid + 1

    else:
        r = mid - 1

print(ans)