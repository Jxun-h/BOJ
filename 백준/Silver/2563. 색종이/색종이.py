from sys import stdin

board = [[0] * 101 for _ in range(101)]
answer = 0

for _ in range(int(stdin.readline())):
    l, b = map(int, stdin.readline().split())

    for i in range(l, l + 10):
        for j in range(b, b + 10):
            board[i][j] = 1

for arr in board:
    answer += arr.count(1)

print(answer)