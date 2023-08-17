from sys import stdin
import heapq

n, m = map(int, stdin.readline().split())
arr, water, dochi, goal = [], [], 0, 0
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

for i in range(n):
    data = list(stdin.readline().rstrip())
    arr.append(data)
    for j in range(m):
        if data[j] == '*':
            water.append((i, j))
        elif data[j] == 'S':
            dochi = (i, j)
        elif data[j] == 'D':
            goal = (i, j)


def mv_water():
    global water
    new_water = []
    for i, j in water:
        for x in range(4):
            nx, ny = dx[x] + i, dy[x] + j
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == '.':
                    arr[nx][ny] = '*'
                    new_water.append((nx, ny))

    water += new_water


def mv_dochi():
    q = []
    heapq.heappush(q, (0, dochi[0], dochi[1]))
    visited = [[True] * m for _ in range(n)]
    visited[dochi[0]][dochi[1]] = False
    for i, j in water:
        visited[i][j] = False

    now_depth = 0
    while q:
        step, i, j = heapq.heappop(q)

        if (i, j) == goal:
            return step

        if step >= now_depth:
            mv_water()
            now_depth += 1

        for x in range(4):
            nx, ny = dx[x] + i, dy[x] + j
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != '*' and arr[nx][ny] != 'X' and visited[nx][ny] is True and arr[nx][ny] != 'S':
                    heapq.heappush(q, (step + 1, nx, ny))
                    visited[nx][ny] = False

    return 'KAKTUS'


print(mv_dochi())
