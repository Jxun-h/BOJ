from sys import stdin
from collections import deque

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())

graph = [[] for _ in range(n + 1)]
for _ in range(int(stdin.readline())):
    k, p = map(int, stdin.readline().split())
    graph[k].append(p)
    graph[p].append(k)


def solve(x):
    q = deque()
    q.append((x, 0))
    visited = set()
    visited.add(x)

    while q:
        now, c = q.popleft()

        if now == b:
            return c

        for i in graph[now]:
            if i not in visited:
                q.append((i, c + 1))
                visited.add(i)

    return False


ans = solve(a)
print(ans) if ans else print(-1)