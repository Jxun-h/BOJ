from sys import stdin

n = int(stdin.readline())
board = []

for _ in range(n):
    board.append(list(stdin.readline().rstrip()))
g_v = [[1] * n for _ in range(n)]
s_v = [[1] * n for _ in range(n)]
g, s = 0, 0


def check(x, y, mode):
    global g, s

    if mode == 1:
        if board[x][y] == board[x][y + 1] and (g_v[x][y] == 1 and g_v[x][y + 1] == 1):
            g += 1
            for j in range(y, n):
                if board[x][j] == 'X':
                    break
                g_v[x][j] = 0
            for j in range(y, -1, -1):
                if board[x][j] == 'X':
                    break
                g_v[x][j] = 0

    elif mode == 2:
        if board[x][y] == board[x + 1][y] and (s_v[x][y] == 1 and s_v[x + 1][y] == 1):
            s += 1
            for i in range(x, n):
                if board[i][y] == 'X':
                    break
                s_v[i][y] = 0

            for i in range(x, -1, -1):
                if board[i][y] == 'X':
                    break
                s_v[i][y] = 0


for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if j + 1 < n:
                check(i, j, 1)

            if i + 1 < n:
                check(i, j, 2)

print(g, s)