from collections import deque
from sys import stdin

n = int(stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))


def bfs():
    q = deque()
    q.append((0, 0, board[0][0]))
    visited = [[1] * n for _ in range(n)]
    visited[0][0] = 0

    while q:
        x, y, mv = q.popleft()

        if x == n - 1 == y:
            return True

        for i in range(2):
            if i == 0:
                nx, ny = mv + x, y
            else:
                nx, ny = x, mv + y

            if -1 < nx < n and -1 < ny < n:
                if visited[nx][ny] == 1:
                    visited[nx][ny] = 0
                    q.append((nx, ny, board[nx][ny]))

    return False


if bfs():
    print("HaruHaru")
else:
    print("Hing")