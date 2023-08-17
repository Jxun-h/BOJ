from collections import deque
from sys import stdin

board = []
n, m = map(int, stdin.readline().split())
for i in range(n):
    board.append(list(stdin.readline().rstrip()))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
visited = set()


def bfs(x, y):
    wolf, sheep = 0, 0

    if board[x][y] == 'k':
        sheep += 1
    elif board[x][y] == 'v':
        wolf += 1

    q = deque()
    q.append((x, y))
    visited.add((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < n and -1 < ny < m:
                if (nx, ny) not in visited:
                    if board[nx][ny] == 'k':
                        sheep += 1
                        q.append((nx, ny))
                        visited.add((nx, ny))

                    elif board[nx][ny] == 'v':
                        wolf += 1
                        q.append((nx, ny))
                        visited.add((nx, ny))

                    elif board[nx][ny] == '.':
                        q.append((nx, ny))
                        visited.add((nx, ny))

    if wolf >= sheep:
        return wolf, 'w'
    else:
        return sheep, 's'


ans = [0, 0]
for i in range(n):
    for j in range(m):
        if board[i][j] != '#' and (i, j) not in visited:
            res, win = bfs(i, j)
            if win == 's':
                ans[0] += res
            else:
                ans[1] += res

print(*ans)