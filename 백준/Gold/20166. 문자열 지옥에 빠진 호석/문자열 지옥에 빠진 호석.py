from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n, m, k = map(int, stdin.readline().split())
ans, arr, res = {}, [], []
dx, dy = [1, 0, -1, 0, 1, 1, -1, -1], [0, 1, 0, -1, -1, 1, 1, -1]

for i in range(n):
    arr.append(list(stdin.readline().rstrip()))

for _ in range(k):
    ans[stdin.readline().rstrip()] = 0


def solve(x, y, cnt, string):
    if cnt == 5:
        return

    if string in ans:
        ans[string] += 1

    for i in range(8):
        nx, ny = (x + n + dx[i]) % n, (y + m + dy[i]) % m
        solve(nx, ny, cnt + 1, string + arr[nx][ny])


for i in range(n):
    for j in range(m):
        start = ''
        solve(i, j, 1, start + arr[i][j])

for key, item in ans.items():
    print(item)
