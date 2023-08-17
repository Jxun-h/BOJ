import heapq
from sys import stdin
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def solve(now, x, y):
    q = []
    heapq.heappush(q, (now, x, y))
    visited = [[1] * n for _ in range(n)]
    visited[x][y] = 0

    while q:
        now, x, y = heapq.heappop(q)

        if x == y == n - 1:
            return now

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny]:
                    visited[nx][ny] = 0
                    heapq.heappush(q, (now + arr[nx][ny], nx, ny))


case = 1
while 1:
    n = int(stdin.readline())
    if n == 0:
        break

    arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

    ans = solve(arr[0][0], 0, 0)
    print('Problem {}:'.format(case), ans)
    case += 1
