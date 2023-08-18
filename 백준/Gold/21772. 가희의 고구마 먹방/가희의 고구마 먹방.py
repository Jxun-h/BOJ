from sys import stdin,setrecursionlimit
setrecursionlimit(10 ** 7)

board = []
pos = False
n, m, t = map(int, stdin.readline().split())
for i in range(n):
    data = list(stdin.readline().rstrip())
    board.append(data)

    if not pos:
        for j in range(m):
            if data[j] == 'G':
                pos = (i, j)

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
ans = 0


def solve(x, y, mv, cnt):
    if mv == t:
        global ans
        ans = max(ans, cnt)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] != '#':
                if board[nx][ny] == 'S':
                    board[nx][ny] = '.'
                    solve(nx, ny, mv + 1, cnt + 1)
                    board[nx][ny] = 'S'
                else:
                    solve(nx, ny, mv + 1, cnt)


solve(pos[0], pos[1], 0, 0)
print(ans)
