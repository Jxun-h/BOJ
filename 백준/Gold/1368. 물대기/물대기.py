from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
q = []
w = []
parent = [x for x in range(n + 1)]
arr = [[0] * (n + 1) for _ in range(n + 1)]


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


for i in range(1, n + 1):
    w.append(int(stdin.readline()))

for i in range(1, n + 1):
    data = list(map(int, stdin.readline().split()))
    for j in range(1, n + 1):
        arr[i][j] = data[j - 1]

        if i != j:
            q.append((data[j - 1], i, j))
        else:
            q.append((w[i - 1], 0, i))

q.sort(key=lambda x: -x[0])

res = 0
while q:
    cost, a, b = q.pop()

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)