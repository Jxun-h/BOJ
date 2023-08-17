from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)


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


n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    k, a, b = map(int, stdin.readline().split())

    if k == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) != find_parent(parent, b):
            print('NO')
        else:
            print('YES')
