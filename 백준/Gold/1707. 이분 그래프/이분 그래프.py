from collections import deque
from sys import stdin


def solve(i):
    q = deque()
    q.append(i)
    visited[i] = 1

    while q:
        now = q.popleft()
        for node in arr[now]:
            if visited[node] == 0:
                q.append(node)
                visited[node] = visited[now] * -1

            elif visited[node] == visited[now]:
                return False

    return True


for _ in range(int(stdin.readline())):
    v, e = map(int, stdin.readline().split())
    arr = [[] for _ in range(v + 1)]
    for __ in range(e):
        a, b = map(int, stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    visited = [0 for _ in range(v + 1)]
    ans = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not solve(i):
                ans = False
                break

    print('YES' if ans else 'NO')