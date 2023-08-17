from sys import stdin
from collections import deque

dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]


def bfs(l):
    q = deque()
    a, b = tuple(map(int, stdin.readline().split()))
    end = tuple(map(int, stdin.readline().split()))
    q.append((a, b, 0))
    board[a][b] = 1

    while q:
        x, y, cost = q.popleft()
        if (x, y) == end:
            return cost
        for i in range(len(dx)):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < l and -1 < ny < l and board[nx][ny] != 1:
                q.append((nx, ny, cost + 1))
                board[nx][ny] = 1


for _ in range(int(stdin.readline())):
    l = int(stdin.readline())
    board = [[0] * l for _ in range(l)]
    print(bfs(l))