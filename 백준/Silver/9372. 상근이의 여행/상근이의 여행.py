from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


for test_case in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    nations = [x for x in range(n + 1)]
    res = 0
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        if find_parent(nations, a) != find_parent(nations, b):
            union_parent(a, b, nations)
            res += 1

    print(res)