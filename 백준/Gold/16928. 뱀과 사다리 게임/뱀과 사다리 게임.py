from sys import stdin
from collections import deque
inf = int(1e9)
n, m = map(int, stdin.readline().split())
ls = [x for x in range(101)]
for _ in range(n + m):
    a, b = map(int, stdin.readline().split())
    ls[a] = b


def bfs():
    visited = [inf for _ in range(101)]
    q = deque([1])
    visited[1] = 0
    while q:
        w = q.popleft()
        if visited[w] >= visited[100]:
            continue
        for i in range(1, 7):
            if w + i > 100:
                continue
            num = ls[w + i]
            if visited[num] >= inf:
                q.append(num)
                visited[num] = visited[w] + 1
    return visited[100]


print(bfs())
