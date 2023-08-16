from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(stdin.readline().rstrip()))


def row(x, y):
    visited[x][y] = 0
    for i in range(y + 1, m):
        if board[x][i] == '-':
            visited[x][i] = 0
        else:
            break
    return 1


def col(x, y):
    for i in range(x + 1, n):
        if board[i][y] == '|':
            visited[i][y] = 0
        else:
            break
    return 1


answer = 0
visited = [[1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if visited[i][j] == 1:
            if board[i][j] == '-':
                answer += row(i, j)
            else:
                answer += col(i, j)

print(answer)
