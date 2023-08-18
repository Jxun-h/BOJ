from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)
import heapq

n, m = map(int, stdin.readline().split())
parent = [x for x in range(n + 1)]
q = []
visited = [False for _ in range(n + 1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


res = 0
total = 0
cnt = 0
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    heapq.heappush(q, (c, a, b))
    total += c

while q:
    c, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += c
        cnt += 1

if cnt == n - 1:
    print(total - res)
else:
    print(-1)