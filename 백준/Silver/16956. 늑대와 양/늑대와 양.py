from collections import deque
from sys import stdin

r, c = map(int, stdin.readline().split())
board = []
wolf = []
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
for i in range(r):
    data = list(stdin.readline().rstrip().replace('.', 'D'))
    board.append(data)
    for j in range(c):
        if data[j] == 'W':
            wolf.append((i, j))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = set()
    visited.add((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (nx, ny) not in visited and board[nx][ny] != 'D' and board[nx][ny] != 'W':
                    if board[nx][ny] == 'S':
                        return False
                    else:
                        visited.add((nx, ny))
                        q.append((nx, ny))

    return True


for x, y in wolf:
    if not bfs(x, y):
        print(0)
        exit()

print(1)
for i in board:
    print(*i, sep='')