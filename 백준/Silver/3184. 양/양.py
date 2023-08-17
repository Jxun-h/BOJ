from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
for n in range(n):
    board.append(list(stdin.readline().rstrip()))
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
visited = set()


def bfs(x, y):
    vo = [set(), set()]
    q = deque()
    q.append((x, y))
    visited.add((x, y))
    while q:
        x, y = q.popleft()

        if board[x][y] == 'o':
            vo[1].add((x, y))
        elif board[x][y] == 'v':
            vo[0].add((x, y))

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < n and -1 < ny < m:
                if board[nx][ny] != '#' and (nx, ny) not in visited:
                    q.append((nx, ny))
                    visited.add((nx, ny))

    if len(vo[0]) < len(vo[1]):
        return 0, len(vo[1])
    else:
        return len(vo[0]), 0


answer = [0, 0]
for i in range(n):
    for j in range(m):
        if (board[i][j] == 'v' or board[i][j] == 'o') and (i, j) not in visited:
            v, o = bfs(i, j)

            answer[0] += o
            answer[1] += v

print(*answer)