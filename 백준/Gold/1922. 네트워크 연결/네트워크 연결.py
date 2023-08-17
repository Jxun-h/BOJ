from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
parent = [x for x in range(n + 1)]
edges = []

for _ in range(m):
    edges.append(list(map(int, stdin.readline().split())))

edges.sort(key= lambda x: x[2])


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


answer = 0
for a, b, c in edges:
    aroot = find_parent(parent, a)
    broot = find_parent(parent, b)

    if aroot != broot:
        if aroot > broot:
            parent[aroot] = broot

        else:
            parent[broot] = aroot

        answer += c

print(answer)