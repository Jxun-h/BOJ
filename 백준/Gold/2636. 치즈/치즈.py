from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
ans = 0
cnt = 0


def melt():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:
                cnt += 1
                board[i][j] = 0
    return cnt


def bfs():
    global ans, cnt
    q = deque()
    q.append((0, 0))
    visited = set()
    visited.add((0, 0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if -1 < nx < n and -1 < ny < m:
                if (nx, ny) not in visited:
                    if board[nx][ny] == 0:
                        q.append((nx, ny))
                        visited.add((nx, ny))
                    elif board[nx][ny] == 1:
                        board[nx][ny] = -1

    melt_cnt = melt()
    if melt_cnt != 0:
        cnt = melt_cnt
    else:
        print(ans)
        print(cnt)
        exit()


while 1:
    bfs()
    ans += 1