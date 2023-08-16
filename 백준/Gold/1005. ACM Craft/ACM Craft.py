from collections import deque
from sys import stdin


def topology_sort(w):
    q = deque()
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = arr[i]

    while q:
        now = q.popleft()

        for node in graph[now]:
            indegree[node] -= 1
            dp[node] = max(dp[now] + arr[node], dp[node])
            if indegree[node] == 0:
                q.append(node)

    return dp[w]


for tc in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    arr = [0] + list(map(int, stdin.readline().split()))
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1

    w = int(stdin.readline())
    print(topology_sort(w))
