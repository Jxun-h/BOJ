from sys import stdin
from collections import deque


n, k = map(int, stdin.readline().split())
network = [[] for _ in range((n + 1))]
tf = True

for i in range(k):
    a, b = map(int, stdin.readline().split())
    network[a].append(b)
    network[b].append(a)


def bfs(root):
    visited = set()
    visited.add(root)
    q = deque()
    q.append((root, 0))

    while q:
        now, dist = q.popleft()
        if dist > 6:
            return False

        for node in network[now]:
            if node not in visited:
                visited.add(node)
                q.append((node, dist + 1))

    if len(visited) == n:
        return True
    else:
        return False


for i in range(1, n + 1):
    if not bfs(i):
        tf = False
        break

if tf:
    print("Small World!")
else:
    print("Big World!")