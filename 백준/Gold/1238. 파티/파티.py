from sys import stdin
import heapq

n, m, x = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
ans = [0 for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))


def solve(start):
    q = []
    heapq.heappush(q, (0, start))
    dist = [int(1e9) for _ in range(n + 1)]
    dist[start] = 0

    while q:
        cost, now = heapq.heappop(q)

        for d, next_pos in graph[now]:
            if dist[next_pos] > cost + d:
                dist[next_pos] = cost + d
                heapq.heappush(q, (cost + d, next_pos))

    return dist


r = -1
for i in range(1, n + 1):
    if i != x:
        go = solve(i)[x]
        goal = solve(x)[i]
        r = max(r, go + goal)

print(r)