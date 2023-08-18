from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
board = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, stdin.readline().split())
    board[a][b] = 1
    board[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])



def solve(chicken):
    visited = [1 for _ in range(n + 1)]
    visited[0] = 0
    for i in range(2):
        visited[chicken[i]] = 0

    res = 0
    for i in range(1, n + 1):
        if visited[i] == 1:
            temp = min(board[i][chicken[0]], board[i][chicken[1]])
            res += temp * 2
            visited[i] = -1

    return res


ans = [-1, -1, int(1e9)]
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        res = solve((i, j))
        if res < ans[2]:
            ans = [i, j, res]

print(*ans)