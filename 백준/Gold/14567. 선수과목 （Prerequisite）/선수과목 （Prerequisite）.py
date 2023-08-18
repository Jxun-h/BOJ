from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
indegree = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
answer = {x: 1 for x in range(1, n + 1)}

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append((i, 1))
        answer[i] = 1

while q:
    now, sem = q.popleft()

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append((i, sem + 1))
            answer[i] = sem + 1

print(*answer.values())
