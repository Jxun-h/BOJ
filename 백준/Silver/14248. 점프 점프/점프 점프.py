from sys import stdin
from collections import deque

n = int(stdin.readline())
arr = [0] + list(map(int, stdin.readline().split()))
graph = [[] for _ in range(n + 1)]
s = int(stdin.readline())
for i in range(1, n + 1):
    if 0 < i + arr[i] < n + 1:
        graph[i].append(i + arr[i])

    if 0 < i - arr[i] < n + 1:
        graph[i].append(i - arr[i])



def solve(s):
    q = deque()
    q.append(s)
    visited = set()

    while q:
        now = q.popleft()
        for x in graph[now]:
            if x not in visited:
                visited.add(x)
                q.append(x)

    return len(visited)

print(solve(s) + 1)