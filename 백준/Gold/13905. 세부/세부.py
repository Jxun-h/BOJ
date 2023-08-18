from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
s, e = map(int, stdin.readline().split())
answer = 0

arr = [[] for _ in range(n + 1)]

for i in range(m):
    h1, h2, k = map(int, stdin.readline().split())
    arr[h1].append((k, h2))
    arr[h2].append((k, h1))


def solve(mid):
    q = deque()
    q.append(s)
    visited = [1 for _ in range(n + 1)]
    visited[s] = 0

    while q:
        now = q.popleft()

        if now == e:
            return True

        for c, node in arr[now]:
            if visited[node] and mid <= c:
                q.append(node)
                visited[node] = 0

    return False


l, r = 1, 1000000

while l <= r:
    mid = (l + r) // 2
    if solve(mid):
        l = mid + 1
        answer = mid
    else:
        r = mid - 1

print(answer)
