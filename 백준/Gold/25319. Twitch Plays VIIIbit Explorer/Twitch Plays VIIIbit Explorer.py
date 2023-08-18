from sys import stdin

n, m, l = map(int, stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(stdin.readline().rstrip()))

target = list(stdin.readline().rstrip())

cnt, cnt_graph, xy = {}, {}, {}
for item in target:
    if item not in cnt:
        cnt[item] = 0
        cnt_graph[item] = 0
        xy[item] = []

    cnt[item] += 1

for x in range(n):
    for y in range(m):
        if graph[x][y] in cnt:
            cnt_graph[graph[x][y]] += 1
            xy[graph[x][y]].append((x, y))

ap = int(1e9)
for i in cnt.keys():
    if ap > cnt_graph[i] // cnt[i]:
        ap = cnt_graph[i] // cnt[i]

x, y, mv = 0, 0, 0
ans = ''

for i in range(ap):
    for item in target:
        nx, ny = xy[item].pop()

        vert = nx - x
        needs = 'D' if vert > 0 else 'U'
        for _ in range(abs(vert)):
            ans += needs

        hori = ny - y
        needs = 'R' if hori > 0 else 'L'
        for _ in range(abs(hori)):
            ans += needs

        ans += 'P'
        mv += abs(vert) + abs(hori) + 1
        x, y = nx, ny

nx, ny = n - 1, m - 1
vert = nx - x
for _ in range(abs(vert)):
    ans += "D"

hori = ny - y
for _ in range(abs(hori)):
    ans += 'R'

mv += abs(vert) + abs(hori)
print(ap, mv)
print(ans)