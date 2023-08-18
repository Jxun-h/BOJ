from sys import stdin

n = int(stdin.readline())
board = [[0] * 101 for _ in range(101)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for _ in range(n):
    x, y, d, g = map(int, stdin.readline().split())

    board[x][y] = 1
    curve = [d]

    for _ in range(g):
        next_curve = []
        for i in range(len(curve)):
            next_curve.append((curve[-i-1] + 1) % 4)

        curve.extend(next_curve)

    for i in curve:
        dx, dy = direction[i]
        nx, ny = x + dx, y + dy
        board[nx][ny] = 1
        x, y = nx, ny

ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            if board[i + 1][j] and board[i][j + 1] and board[i + 1][j + 1]:
                ans += 1

print(ans)