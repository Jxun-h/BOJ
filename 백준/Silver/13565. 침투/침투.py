from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
board = []
visited = set()
for _ in range(n):
    board.append(list(map(int, list(stdin.readline().rstrip()))))

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
res_tf = False


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited.add((x, y))

    while q:
        x, y = q.popleft()
        if x == n - 1:
            return True

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if -1 < nx < n and -1 < ny < m and (nx, ny) not in visited:
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                    visited.add((nx, ny))


for j in range(m):
    if board[0][j] == 0 and (0, j) not in visited:
        if bfs(0, j) is True:
            res_tf = True
            break

print('YES') if res_tf else print('NO')
