from sys import stdin
from collections import deque

visited = [1] * 1000001
arr = []
for _ in range(5):
    arr.append(list(map(int, stdin.readline().split())))
ans = 0
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]


def solve(x, y):
    q = deque()
    cnt = 1
    q.append((cnt, x, y, '' + str(arr[x][y])))

    while q:
        cnt, x, y, now = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if cnt < 6:
                    if cnt + 1 == 6:
                        if visited[int(now + str(arr[nx][ny]))]:
                            visited[int(now + str(arr[nx][ny]))] = 0
                            global ans
                            ans += 1
                    else:
                        q.append((cnt + 1, nx, ny, now + str(arr[nx][ny])))


for i in range(5):
    for j in range(5):
        solve(i, j)

print(ans)