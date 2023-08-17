from sys import stdin

case = 1


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a != b:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b


while 1:
    answer = ''
    n, m = map(int, stdin.readline().split())
    parent = [x for x in range(n + 1)]
    cycle = set()
    group = set()
    res = 0

    if n == m == 0:
        break

    for _ in range(m):
        a, b = map(int, stdin.readline().split())

        A, B = find_parent(parent, a), find_parent(parent, b)
        if A != B:
            union_parent(parent, a, b)
        else:
            cycle.add(a)

    for i in range(n + 1):
        find_parent(parent, i)

    for i in cycle:
        group.add(parent[i])

    for i in range(1, n + 1):
        if parent[i] in group:
            continue

        res += 1
        group.add(parent[i])

    if res == 1:
        print("Case {}: There is one tree.".format(case))

    elif res > 1:
        print("Case {}: A forest of {} trees.".format(case, res))

    else:
        print("Case {}: No trees.".format(case))

    case += 1
