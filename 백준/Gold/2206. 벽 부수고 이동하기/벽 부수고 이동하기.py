from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, list(stdin.readline().rstrip()))))

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def bfs():
    global res
    q = deque()
    q.append((0, 0, 1))
    visited = [[[0] * 2 for _ in range(m)] for __ in range(n)]
    visited[0][0][1] = 1

    while q:
        x, y, c = q.popleft()
        if (n-1, m-1) == (x, y):
            return visited[x][y][c]

        for pos in range(4):
            nx, ny = x + dx[pos], y + dy[pos]
            if -1 < nx < len(board) and -1 < ny < len(board[0]):
                if board[nx][ny] == 1 and c == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    q.append([nx, ny, 0])

                elif visited[nx][ny][c] == 0 and board[nx][ny] == 0:
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    q.append((nx, ny, c))

    return -1


print(bfs())