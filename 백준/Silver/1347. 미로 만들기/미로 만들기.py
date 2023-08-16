from sys import stdin

n = int(stdin.readline())
command = stdin.readline().rstrip()
pos = [(0, 0)]
direction = 2
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

for c in command:
    if c == 'R':
        direction = (direction + 1) % 4

    elif c == 'L':
        direction = (direction - 1) if direction != 0 else 3

    else:
        x = pos[-1][0] + dx[direction]
        y = pos[-1][1] + dy[direction]
        pos.append((x, y))

x_sort = sorted(pos, key=lambda x: x[0])
y_sort = sorted(pos, key=lambda x: x[1])
x_min, x_max = x_sort[0][0], x_sort[-1][0]
y_min, y_max = y_sort[0][1], y_sort[-1][1]

board = [['#' for i in range(y_min, y_max + 1)] for j in range(x_min, x_max + 1)]

for i in range(len(pos)):
    pos[i] = (pos[i][0] - x_min, pos[i][1] - y_min)

for i, j in pos:
    board[i][j] = '.'

for b in board:
    print(*b, sep='')