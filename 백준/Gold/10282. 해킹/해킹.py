from sys import stdin
import heapq


def bfs(start, inf):
    q = []
    t = 0
    heapq.heappush(q, (t, start))
    dp = [inf for _ in range(n + 1)]
    dp[start] = 0

    while q:
        time, now = heapq.heappop(q)
        for tc, next_node in arr[now]:
            temp = tc + time
            if temp < dp[next_node]:
                dp[next_node] = temp
                heapq.heappush(q, (tc + time, next_node))

    return dp


for _ in range(int(stdin.readline())):
    n, d, c = map(int, stdin.readline().split())
    arr = [[] for _ in range(n + 1)]
    inf = int(1e9)
    for i in range(d):
        a, b, s = map(int, stdin.readline().split())
        arr[b].append((s, a))

    res = bfs(c, inf)
    max_ans, cnt = 0, 0
    for i in res:
        if i != inf:
            if max_ans < i:
                max_ans = i
            cnt += 1
    print(cnt, max_ans)