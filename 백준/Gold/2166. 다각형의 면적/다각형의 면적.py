from sys import stdin
edges = []
step = int(stdin.readline())
for i in range(step):
    edges.append(list(map(int, stdin.readline().split())))
edges.append(edges[0])

a, b = 0, 0
for i in range(step):
    a += edges[i][0] * edges[i + 1][1]
    b += edges[i][1] * edges[i + 1][0]

if b > a:
    print(round((a + b) / 2, 1))
else:
    print(round((a - b) / 2, 1))