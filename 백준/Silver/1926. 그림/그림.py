from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

visited = [[1] * m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def bfs(x, y, width):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < n and -1 < ny < m:
                if visited[nx][ny] == 1 and board[nx][ny] == 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 0
                    width += 1

    return width


ans, cnt = 0, 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1 and board[i][j] == 1:
            cnt += 1
            ans = max(ans, bfs(i, j, 1))

print(cnt, ans, end='\n')