from sys import stdin
import heapq

n = int(stdin.readline())
arr = [[1] * n for _ in range(n)]
x, y, gx, gy = map(int, stdin.readline().split())
dx, dy = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]


def solve(x, y, gx, gy):
    q = []
    heapq.heappush(q, (0, x, y))
    arr[x][y] = 0

    while q:
        cost, x, y = heapq.heappop(q)
        if (x, y) == (gx, gy):
            return cost

        for i in range(6):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny]:
                    heapq.heappush(q, (cost + 1, nx, ny))
                    arr[nx][ny] = 0

    return -1


print(solve(x, y, gx, gy))