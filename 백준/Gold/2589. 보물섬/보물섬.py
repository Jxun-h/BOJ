from collections import deque
from sys import stdin
import heapq

# 보물의 위치(어느 땅의 좌표에서 어느 땅까지 좌표간의 거리 계산) -> max 값인 곳으로
# 피타고라스 빗변 길이 = 좌표간의 거리

n, m = map(int, stdin.readline().split())
lands = []
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

arr = []
for i in range(n):
    data = list(stdin.readline().rstrip())
    for j in range(m):
        if data[j] == 'L':
            lands.append((i, j))
    arr.append(data)


def find_treasure(origin_i, origin_j):
    q = deque()
    dist = 0
    q.append((dist, origin_i, origin_j))
    finded_treasure[origin_i][origin_j] = True
    treasure, max_dist = [], 0

    while q:
        dist, x, y = q.popleft()
        if dist > max_dist:
            max_dist = dist
            treasure = [(origin_i, origin_j), (x, y)]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'L' and finded_treasure[nx][ny] is False:
                    q.append((dist + 1, nx, ny))
                    finded_treasure[nx][ny] = True

    return dist, treasure


# 한 보물에서 다른 보물의 최단거리 = BFS
def find_road(t):
    i, j = t[0]
    gx, gy = t[1]
    q = []
    visited = [[False for _ in range(m)] for __ in range(n)]
    dist = 0
    heapq.heappush(q, (dist, i, j))
    visited[i][j] = True

    while q:
        dist, x, y = heapq.heappop(q)

        if (x, y) == (gx, gy):
            print(dist)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 'L' and visited[nx][ny] is False:
                    heapq.heappush(q, (dist + 1, nx, ny))
                    visited[nx][ny] = True


dist, t = 0, []
lands.sort()
for i, j in lands:
    finded_treasure = [[False] * m for __ in range(n)]
    if finded_treasure[i][j]:
        continue
    else:
        _dist, _t = find_treasure(i, j)
        if _dist > dist:
            dist = _dist
            t = _t

find_road(t)