from sys import stdin
import math


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        parent[b] = a


n, m = map(int, stdin.readline().split())
parent = [x for x in range(n)]
xys = []
edges = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    xys.append((x, y))

connected_cnt = 0
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    if find_parent(parent, x - 1) != find_parent(parent, y - 1):
        union_parent(parent, x - 1, y - 1)
        connected_cnt += 1

for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = xys[i]
        x2, y2 = xys[j]
        dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
        edges.append((dist, i, j))

edges.sort(key=lambda x: x[0])

ans = 0
for dist, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        ans += dist
        connected_cnt += 1

    if connected_cnt == n - 1:
        break

print('%.2f' % ans)
