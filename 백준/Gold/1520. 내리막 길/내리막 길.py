from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, stdin.readline().split())))

dp = [[-1] * m for _ in range(n)]
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]


def solve(x, y):
    global ans

    if (x, y) == (n - 1, m - 1):
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board[x][y] > board[nx][ny]:
                dp[x][y] += solve(nx, ny)

    return dp[x][y]


print(solve(0, 0))
