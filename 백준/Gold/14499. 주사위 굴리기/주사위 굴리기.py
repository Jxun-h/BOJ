from sys import stdin

n, m, x, y, command_nums = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

command = list(map(int, stdin.readline().split()))

dice = [0 for _ in range(6)]
dice[0] = board[x][y]

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for c in command:
    nx, ny = x + dx[c - 1], y + dy[c - 1]
    if 0 <= nx < n and 0 <= ny < m:
        if c == 1:
            dice[4], dice[5], dice[2], dice[0] = dice[0], dice[4], dice[5], dice[2]

        elif c == 2:
            dice[2], dice[5], dice[4], dice[0] = dice[0], dice[2], dice[5], dice[4]

        elif c == 3:
            dice[1], dice[5], dice[3], dice[0] = dice[0], dice[1], dice[5], dice[3]

        elif c == 4:
            dice[3], dice[5], dice[1], dice[0] = dice[0], dice[3], dice[5], dice[1]

        if board[nx][ny] == 0:
            board[nx][ny] = dice[0]

        else:
            dice[0] = board[nx][ny]
            board[nx][ny] = 0

        x, y = nx, ny
        print(dice[5])
