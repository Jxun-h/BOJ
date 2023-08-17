import heapq
from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
nums = set()

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
    nums.add(a)


def solve():
    res = []
    q = []
    for x in range(1, n + 1):
        if indegree[x] == 0:
            heapq.heappush(q, x)

    while q:
        cur = heapq.heappop(q)
        res.append(cur)

        for k in graph[cur]:
            indegree[k] -= 1
            if indegree[k] == 0:
                heapq.heappush(q, k)
    return res


answer = solve()
print(*answer)
