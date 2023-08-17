from collections import deque
from sys import stdin

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def solve():
    global hq, fq
    while hq:
        next_pos = deque()
        while hq:
            x, y = hq.popleft()

            if (x == row - 1 or y == col - 1 or x == 0 or y == 0) and board[x][y] != '*':
                return board[x][y]

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < row and -1 < ny < col:
                    if board[nx][ny] == '.' and board[x][y] != '*':
                        next_pos.append((nx, ny))
                        board[nx][ny] = board[x][y] + 1

        hq = next_pos

        next_pos = deque()
        while fq:
            x, y = fq.popleft()

            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if -1 < nx < row and -1 < ny < col:
                    if board[nx][ny] != '#' and visited[nx][ny]:
                        next_pos.append((nx, ny))
                        visited[nx][ny] = 0
                        board[nx][ny] = '*'

        fq = next_pos


for _ in range(int(stdin.readline())):
    col, row = map(int, stdin.readline().split())
    board = []
    hq, fq = deque(), deque()
    visited = [[1] * col for _ in range(row)]

    for x in range(row):
        data = list(stdin.readline().rstrip())
        board.append(data)
        for y in range(col):
            if data[y] == '@':
                data[y] = 0
                hq.append((x, y))

            if data[y] == '*':
                fq.append((x, y))
                visited[x][y] = 0

    ans = solve()
    print(ans + 1 if ans is not None else 'IMPOSSIBLE')
