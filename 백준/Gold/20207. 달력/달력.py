from sys import stdin

n = int(stdin.readline())
board = [0] * 366
last_days = 0

for _ in range(n):
    s, e = map(int, input().split(' '))
    last_days = max(last_days, e)
    for i in range(s, e + 1):
        board[i] += 1

row, col, res = 0, 0, 0

for i in range(1, last_days + 1):
    if board[i] != 0:
        row = max(row, board[i])
        col += 1
    else:
        res += row * col
        row = 0
        col = 0

res += row * col
print(res)