from collections import deque
from sys import stdin

n, m = map(int, stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(stdin.readline().rstrip()))

cross_cnt, cross_ans = 0, []
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]
star_n = 0
visited = [[0] * m for _ in range(n)]
ans = []


def bfs(x, y):
    q = deque()

    for i in range(4):
        nx, ny = dx[i] + x, dy[i] + y
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
            q.append((nx, ny, i))

        if len(q) == 4:
            visited[x][y] = 1

    length = 1
    while len(q) == 4:
        ans.append((x + 1, y + 1, length))

        for k in range(4):
            i, j, d = q.popleft()
            visited[i][j] = 1
            nx, ny = dx[d] + i, dy[d] + j
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '*':
                q.append((nx, ny, k))

        length += 1


for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            star_n += 1
            bfs(i, j)

star_sum = 0
for i in visited:
    star_sum += sum(i)

if len(ans) == 0 or star_n != star_sum:
    print(-1)
else:
    print(len(ans))
    for i in ans:
        print(*i)
