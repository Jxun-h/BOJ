from collections import deque
from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


def get_cnt(x, graph, visited):
    q = deque()
    q.append(x)
    visited.add(x)

    while q:
        now = q.popleft()

        for y in list(graph[now]):
            if y not in visited:
                q.append(y)
                visited.add(y)

    return 1


def solve(cnt, temp):
    global ans
    res = 0
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        graph[temp[i]].append(arr[i])

    visited = set()
    for i in range(1, n + 1):
        if i not in visited:
            res += get_cnt(i, graph, visited)

    ans = max(res, ans)


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    ans = 0

    solve(0, [x for x in range(1, n + 1)])
    print(ans)
