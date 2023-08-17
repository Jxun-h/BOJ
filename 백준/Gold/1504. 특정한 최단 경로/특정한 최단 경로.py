from sys import stdin
import heapq

n, e = map(int, stdin.readline().split())
nodes = [[] for _ in range(n + 1)]

for i in range(e):
    a, b, c = map(int, stdin.readline().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

o, p = map(int, stdin.readline().split())


def solve(s):
    dist = [int(1e9) for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0, s))
    dist[s] = 0

    while q:
        d, now = heapq.heappop(q)

        if dist[now] > d:
            continue

        for i in nodes[now]:
            cost = d + i[1]

            if dist[i[0]] > cost:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist


origin = solve(1)
o_dijk = solve(o)
p_dijk = solve(p)
ans = min((origin[o] + o_dijk[p] + p_dijk[n]), (origin[p] + p_dijk[o] + o_dijk[n]))

if ans >= int(1e9):
    print(-1)
else:
    print(ans)