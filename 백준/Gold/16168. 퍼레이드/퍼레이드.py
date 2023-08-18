from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if level[a] >= level[b]:
        parent[b] = a
        if level[a] == level[b]:
            level[a] += 1

    else:
        parent[a] = b


v, e = map(int, stdin.readline().split())
graph = [[] * (v + 1) for _ in range(v + 1)]
level = [0 for _ in range(v + 1)]
parent = [x for x in range(v + 1)]

for _ in range(e):
    a, b = map(int, stdin.readline().split())

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

    if a > b:
        a, b = b, a

    graph[a].append(b)
    graph[b].append(a)

pivot = find_parent(parent, 1)

for i in range(2, v + 1):
    if pivot != find_parent(parent, i):
        print('NO')
        exit()

cnt = 0
for s in range(1, v + 1):
    if len(graph[s]) & 1:
        cnt += 1

print('YES' if cnt == 2 or not cnt else 'NO')