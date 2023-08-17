from sys import stdin


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def get_dist(i, j):
    return (xys[i][0] - xys[j][0]) ** 2 + (xys[i][1] - xys[j][1]) ** 2


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    parent = [x for x in range(n)]
    xys = []
    for _ in range(n):
        xys.append(list(map(int, stdin.readline().split())))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue

            dist = get_dist(i, j)
            rad = (xys[i][2] + xys[j][2]) ** 2

            if dist <= rad and find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)

    visited = [True for x in range(n)]
    ans = 0
    for i in range(n):
        t = find_parent(parent, i)
        if visited[t]:
            ans += 1
            visited[t] = False
    
    print(ans)