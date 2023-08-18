from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
arr, shark = [], []
dx, dy = [1, 0, 0, -1, 1, -1, 1, -1], [0, 1, -1, 0, 1, -1, -1, 1]
ans = -1

for i in range(n):
    data = list(map(int, stdin.readline().split()))
    arr.append(data)
    for j in range(m):
        if data[j] == 1:
            shark.append((i, j))


def solve(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    visited = set()
    visited.add((x, y))

    while q:
        dist, x, y = heapq.heappop(q)
        if arr[x][y] == 1:
            return dist

        for i in range(8):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    heapq.heappush(q, (dist + 1, nx, ny))
                    visited.add((nx, ny))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            res = solve(i, j)
            if res > ans:
                ans = res

print(ans)
