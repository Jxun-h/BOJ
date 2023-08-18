from sys import stdin

n, m = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
arr = []
direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
res = 0


def solve(r, c, d):
    global res
    if arr[r][c] == 0:
        arr[r][c] = 2
        res += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx, ny = direction[nd][0] + r, direction[nd][1] + c
        if arr[nx][ny] == 0:
            solve(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx, ny = direction[nd][0] + r, direction[nd][1] + c
    if arr[nx][ny] == 1:
        return
    solve(nx, ny, d)


solve(r, c, d)
print(res)