from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(int(1e9))

n = int(stdin.readline())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, stdin.readline().split())
    tree[a].append((b, c))
    tree[b].append((a, c))


def bfs(i):
    visited = set()
    q = deque()
    q.append((i, 0))
    visited.add(i)
    res = (0, 0)

    while q:
        now, cost = q.popleft()
        for n, c in tree[now]:
            if n not in visited:
                visited.add(n)
                t = c + cost
                q.append((n, t))

                if res[1] < t:
                    res = (n, t)

    return res


a = bfs(1)
b = bfs(a[0])
print(b[1])