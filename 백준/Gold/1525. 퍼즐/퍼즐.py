from collections import deque
from sys import stdin

arr = []
c = [1, 2, 3, 4, 5, 6, 7, 8, 0]
x, y = 0, 0
for i in range(3):
    data = list(map(int, stdin.readline().split()))
    arr.append(data)
    for j in range(3):
        if data[j] == 0:
            x, y = i, j

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]


def swap(a, b): return b, a


def solve(x, y):
    q = deque()
    temp = []
    for p in arr:
        temp.extend(p)

    q.append((0, x, y, temp))
    visited = set()

    while q:
        cnt, x, y, check_list = q.popleft()
        # visited.discard(tuple(check_list))
        if check_list == c:
            return cnt

        else:
            temp = [check_list[idx:idx + 3] for idx in range(0, 7, 3)]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 3 and 0 <= ny < 3:

                    temp[x][y], temp[nx][ny] = swap(temp[x][y], temp[nx][ny])

                    concat_list = []
                    for i in temp:
                        concat_list.extend(i)

                    if tuple(concat_list) not in visited:
                        visited.add(tuple(concat_list))
                        q.append((cnt + 1, nx, ny, concat_list))
                    temp[x][y], temp[nx][ny] = swap(temp[x][y], temp[nx][ny])

    return -1


print(solve(x, y))
