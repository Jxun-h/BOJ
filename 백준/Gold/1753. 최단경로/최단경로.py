import heapq
from sys import stdin

n, m = map(int, stdin.readline().split())
start = int(stdin.readline())
graph = {x: {} for x in range(1, n + 1)}

for _ in range(m):
    f, t, c = map(int, stdin.readline().split())
    if t in graph[f]:
        if graph[f][t] > c:
            graph[f][t] = c
    else:
        graph[f][t] = c


def solve(root):
    distance = {node: int(1e9) for node in graph.keys()}
    q = []
    heapq.heappush(q, (0, root))

    while q:
        cost, now = heapq.heappop(q)
        if distance[now] < cost:
            continue

        for node, dist in graph[now].items():
            w_dist = dist + cost
            if w_dist < distance[node]:
                distance[node] = w_dist
                heapq.heappush(q, (w_dist, node))

    return distance


distance = solve(start)
for i in range(1, n+1):
    if i == start:
        print(0)
    else:
        print(distance[i]) if distance[i] != int(1e9) else print('INF')